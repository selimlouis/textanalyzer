function getWords(text){
    var totalwords = text.split(' ');
    var words = [];
    for(var i = 0; i < totalwords.length; i++){
        if(totalwords[i] !== ' '){
            words.push(totalwords[i]);
        }
    }
    return words;
}

function getCountedWords(words){
    var wordsMap = {};
    /*
        wordsMap = {
        'Oh': 2,
        'Feelin': 1,
        ...
        }
    */
    words.forEach(function (key) {
        if (wordsMap.hasOwnProperty(key.toLowerCase())) {
        wordsMap[key.toLowerCase()]++;
        } else {
        wordsMap[key.toLowerCase()] = 1;
        }
    });
    return wordsMap; 
}

function sortByCount (wordsMap) {

    // sort by count in descending order
    var finalWordsArray = [];
    finalWordsArray = Object.keys(wordsMap).map(function (key) {
    return {
        name: key,
        total: wordsMap[key]
    };
    });

    finalWordsArray.sort(function (a, b) {
    return b.total - a.total;
    });

    return finalWordsArray;
}

//gets an array of dics returns keys
function getSortedMap(finalWordsArray){
    var sortedMap = {};
    
    finalWordsArray.forEach( function (object) {
        sortedMap[object.name] = object.total;
    })

    return sortedMap;
}

function getPerfectZipf(count){
    var result = [];
    for(var i = 1; i <= count; i++){
        result.push(1 / i);
    }
    return result;
}

function getWordZipf(counts){
    var mostcounted = counts[0];

    var result = [];
    for(var i = 0; i <=counts.length; i++){
        result.push(1/ (mostcounted/counts[i]));
    }
    return result;
}

function analyzeText(text){
    //var text = document.getElementById("input1").value;

    var words = getWords(text);
    var wordcount = words.length - 1;
    var wordsMap = getCountedWords(words);
    var finalWordsArray = sortByCount(wordsMap);
    var sortedMap = getSortedMap(finalWordsArray.slice(0,10));

    document.getElementById("p1").innerHTML = wordcount;

    
    var ctx = document.getElementById('myChart').getContext('2d');
    var chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: Object.keys(sortedMap),
            datasets: [{
                label: 'Words',
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: Object.values(sortedMap),
                backgroundColor: "lightgreen",
                borderColor: "lightgreen"
            }]
        },
    });

    var ctx2 = document.getElementById('myComparison').getContext('2d');
    var chart2 = new Chart(ctx2, {
        type: 'line',
        data: {
            labels: Object.keys(sortedMap),
            datasets: [{
                label: 'Perfect Zipf',
                data: getPerfectZipf(10),
                borderColor: "lightblue",
                fill: false
            },{
                label: 'Word Zipf',
                data: getWordZipf(Object.values(sortedMap)),
                borderColor: "lightgreen",
                fill: false,
                cubicInterpolationMode: 'monotone'
            }
            ]
        },
        // Configuration options go here
        options: {}
    });


}


function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
}