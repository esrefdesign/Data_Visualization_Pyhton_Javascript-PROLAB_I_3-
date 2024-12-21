// Sayfaya yan tarafta butonları ekleyen bir işlev
function createSidebarButtons() {
    // Sağ tarafa bir div ekle (butonları içerecek)
    const sidebar = document.createElement('div');
    sidebar.id = 'buttonSidebar';
    sidebar.style.position = 'absolute';
    sidebar.style.top = '10%';
    sidebar.style.right = '10px';
    sidebar.style.width = '100px';
    sidebar.style.display = 'flex';
    sidebar.style.flexDirection = 'column';
    sidebar.style.gap = '10px';
    sidebar.style.zIndex = '9999';

    // Buton bilgileri (id ve metin olarak)
    const buttonData = [
        { id: 'button1', text: '1. İSTER' },
        { id: 'button2', text: '2. İSTER' },
        { id: 'button3', text: '3. İSTER' },
        { id: 'button4', text: '4. İSTER' },
        { id: 'button5', text: '5. İSTER' },
        { id: 'button6', text: '6. İSTER' },
        { id: 'button7', text: '7. İSTER' }
    ];

    // Butonları oluştur ve ekle
    buttonData.forEach(buttonInfo => {
        const button = document.createElement('button');
        button.id = buttonInfo.id;
        button.innerText = buttonInfo.text;
        button.style.padding = '10px';
        button.style.fontSize = '14px';
        button.style.cursor = 'pointer';
        button.style.border = '1px solid #000';
        button.style.backgroundColor = '#ffffff';
        button.style.color = '#000';
        button.style.borderRadius = '5px';

        // Örnek bir tıklama olayı
        button.onclick = () => alert(`${buttonInfo.text} butonuna tıklandı!`);

        sidebar.appendChild(button);
    });

    // Sidebar'ı body'e ekle
    document.body.appendChild(sidebar);
}

function setupButtonActions(graphData) {
    // 1. A ile B arasındaki en kısa yol
    document.getElementById('button1').onclick = () => {
        const authorA = prompt("A yazarının ID'sini giriniz:");
        const authorB = prompt("B yazarının ID'sini giriniz:");
        
        if (authorA && authorB) {
            // En kısa yol algoritmasını çağır
            const shortestPath = findShortestPath(graphData, authorA, authorB);
            if (shortestPath) {
                alert(`En kısa yol: ${shortestPath.join(" -> ")}`);
                visualizePath(shortestPath); // Grafikte göster
            } else {
                alert("A ile B arasında bir yol bulunamadı.");
            }
        }
    };

    // 2. A ve işbirliği yaptığı yazarlar için düğüm ağırlıklarına göre kuyruk
    document.getElementById('button2').onclick = () => {
        const authorA = prompt("A yazarının ID'sini giriniz:");
        if (authorA) {
            const queue = createWeightedQueue(graphData, authorA);
            visualizeQueue(queue);
        }
    };

    // 3. Kuyruktan BST oluşturma
    document.getElementById('button3').onclick = () => {
        const authorA = prompt("A yazarının ID'sini giriniz:");
        if (authorA) {
            const bst = createBSTFromQueue(graphData, authorA);
            visualizeBST(bst);
        }
    };

    // 4. Kısa yolların hesaplanması
    document.getElementById('button4').onclick = () => {
        const authorA = prompt("A yazarının ID'sini giriniz:");
        if (authorA) {
            const shortestPaths = calculateAllShortestPaths(graphData, authorA);
            visualizeTable(shortestPaths);
        }
    };

    // 5. İşbirliği yaptığı yazar sayısının hesaplanması
    document.getElementById('button5').onclick = async () => {
        const authorA = prompt("A yazarının ID'sini giriniz:"); // Kullanıcıdan yazar ID'sini al
        if (authorA) {
            try {
                // Flask API'ye POST isteği gönder
                const response = await fetch("http://127.0.0.1:5000/wanted_5", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"  // JSON formatını belirle
                    },
                    body: JSON.stringify({ author_name: authorA })  // JSON verisini gönder
                });
    
                if (!response.ok) {
                    const errorData = await response.json();
                    alert(`Hata: ${errorData.error || "Bilinmeyen bir hata oluştu."}`);
                    return;
                }
    
                const data = await response.json(); // API'den dönen yanıtı al
                alert(`${authorA} yazarının toplam işbirliği yaptığı yazar sayısı: ${data.coauthor_count}`);
            } catch (error) {
                console.error("Fetch hatası:", error);
                alert("Bir hata oluştu. Lütfen bağlantınızı kontrol edin.");
            }
        }
    };

    // 6. En çok işbirliği yapan yazarın belirlenmesi
    document.getElementById('button6').onclick = () => {
        const mostCollaborativeAuthor = findMostCollaborativeAuthor(graphData);
        alert(`En çok işbirliği yapan yazar: ${mostCollaborativeAuthor.name}, İşbirlikçi sayısı: ${mostCollaborativeAuthor.count}`);
    };

    // 7. En uzun yolun bulunması
    document.getElementById('button7').onclick = () => {
        const authorA = prompt("A yazarının ID'sini giriniz:");
        if (authorA) {
            const longestPath = findLongestPath(graphData, authorA);
            alert(`En uzun yol: ${longestPath.join(" -> ")}`);
            visualizePath(longestPath);
        }
    };
}

// Bu işlevi sayfa yüklenirken çağırın ve graphData'yı geçin
window.onload = () => {
    createSidebarButtons();
    const graphData = loadGraphData(); // Mevcut grafiği yükleyen bir işlev
    setupButtonActions(graphData);
};

// Grafiği, yolları ve diğer işlemleri göstermek için gereken ek yardımcı işlevleri aşağıda tanımlayın
function findShortestPath(graphData, authorA, authorB) {
    const visited = new Set();
    const queue = [[authorA]];  // Yolları kuyruk olarak saklıyoruz.

    while (queue.length > 0) {
        const path = queue.shift();
        const node = path[path.length - 1];  // Son düğümü alıyoruz.

        if (node === authorB) {
            return path;  // Eğer hedefe ulaşıldıysa, yolu döndür.
        }

        if (!visited.has(node)) {
            visited.add(node);
            const neighbors = graphData[node] || [];  // Komşuları alıyoruz.

            for (let neighbor of neighbors) {
                const newPath = [...path, neighbor];  // Yeni yolu oluştur.
                queue.push(newPath);  // Kuyruğa yeni yolu ekle.
            }
        }
    }

    return null;  // Yol bulunamazsa null döndür.
}


function createWeightedQueue(graphData, authorA) {
    const queue = [];

    // Yazarın tüm komşularını al
    const neighbors = graphData[authorA] || [];

    // Komşuları, bağlantı sayılarına göre sıralıyoruz.
    for (let neighbor of neighbors) {
        queue.push({ author: neighbor, weight: graphData[neighbor].length });
    }

    queue.sort((a, b) => b.weight - a.weight);  // Ağırlığa göre azalan sırada sıralıyoruz.
    return queue;
}


function createBSTFromQueue(graphData, authorA) {
    const queue = createWeightedQueue(graphData, authorA);
    let bst = null;

    // Kuyruğu işleyerek BST oluşturuyoruz.
    queue.forEach(item => {
        bst = insertBST(bst, item);
    });

    return bst;

    // BST'ye eleman eklemek için yardımcı fonksiyon.
    function insertBST(node, item) {
        if (!node) return { value: item, left: null, right: null };

        if (item.weight < node.value.weight) {
            node.left = insertBST(node.left, item);
        } else {
            node.right = insertBST(node.right, item);
        }
        return node;
    }
}


function calculateAllShortestPaths(graphData, authorA) {
    const allPaths = {};
    const visited = new Set();
    const queue = [[authorA]];

    while (queue.length > 0) {
        const path = queue.shift();
        const node = path[path.length - 1];

        if (!visited.has(node)) {
            visited.add(node);
            allPaths[node] = path;  // Bu yolu sakla

            const neighbors = graphData[node] || [];
            for (let neighbor of neighbors) {
                const newPath = [...path, neighbor];
                queue.push(newPath);
            }
        }
    }

    return allPaths;  // Tüm yolları döndür.
}


function countCollaborators(graphData, authorA) {
    const collaborators = new Set(graphData[authorA] || []);
    return collaborators.size;
}


function findMostCollaborativeAuthor(graphData) {
    let maxCollaborations = 0;
    let mostCollaborativeAuthor = null;

    for (let author in graphData) {
        const collaborations = graphData[author].length;
        if (collaborations > maxCollaborations) {
            maxCollaborations = collaborations;
            mostCollaborativeAuthor = { name: author, count: collaborations };
        }
    }

    return mostCollaborativeAuthor;
}


function findLongestPath(graphData, authorA) {
    let longestPath = [];
    const visited = new Set();

    function dfs(node, path) {
        if (visited.has(node)) return;
        visited.add(node);

        if (path.length > longestPath.length) {
            longestPath = [...path];
        }

        const neighbors = graphData[node] || [];
        for (let neighbor of neighbors) {
            dfs(neighbor, [...path, neighbor]);
        }
    }

    dfs(authorA, [authorA]);
    return longestPath;
}


function visualizePath(path) {
    // Grafikte yolu gösterme
}

function visualizeQueue(queue) {
    // Kuyruğu canlı olarak gösterme
}

function visualizeBST(bst) {
    // BST'yi grafikte gösterme
}

function visualizePath(path) {
    alert(`Yol: ${path.join(" -> ")}`);
}

function visualizeQueue(queue) {
    alert(`Kuyruk: ${queue.map(item => `${item.author}: ${item.weight}`).join(" | ")}`);
}

function visualizeBST(bst) {
    const displayBST = (node) => {
        if (!node) return "";
        return `(${displayBST(node.left)}) ${node.value.author} (${displayBST(node.right)})`;
    };
    alert(`BST: ${displayBST(bst)}`);
}

function visualizeTable(shortestPaths) {
    let tableContent = "Yazar\t\tYol\n";
    for (let author in shortestPaths) {
        tableContent += `${author}\t\t${shortestPaths[author].join(" -> ")}\n`;
    }
    alert(tableContent);
}


function loadGraphData() {
    // Python'dan gelen grafiği JSON formatında yükleme
    return {}; // Örnek JSON verisi
}


// Sayfa yüklendiğinde butonları ekle
//window.onload = createSidebarButtons;


