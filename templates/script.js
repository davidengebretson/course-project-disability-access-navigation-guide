function loadSearchData(){
    let buildings = [
        'arntzenhall',
        'biologybuilding',
        'enviornmentalscience',
        'fineartsbuilding',
        'interdiciplinaryscience',
        'morsehall',
        'parkshall',
        'rossengineeringtech',
        'sciencelecturebuilding',
        'bondhall',
        'carvergym',
        'collegehall',
        'fraserhall',
        'haggardhall'
    ];
    
    let list = document.getElementById('list');
    // Add each data item as an <a> tag
    buildings.forEach((building)=>{
        let a = document.createElement("a");
        a.innerText = building;
        a.classList.add("listItem");
        list.appendChild(a);
    })
}