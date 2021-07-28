function load_checkboxes() {
    for (let i = 0; i < america.length; i++)
        createCheckbox(america[i], 'america');
    document.getElementById('america').checked = true;

    for (let i = 0; i < asia.length; i++)
        createCheckbox(asia[i], 'asia');
    document.getElementById('asia').checked = true;

    for (let i = 0; i < africa.length; i++)
        createCheckbox(africa[i], 'africa');
    document.getElementById('africa').checked = true;

    for (let i = 0; i < oceania.length; i++)
        createCheckbox(oceania[i], 'oceania');
    document.getElementById('oceania').checked = true;

    for (let i = 0; i < europe.length; i++)
        createCheckbox(europe[i], 'europe');
    document.getElementById('europe').checked = true;
}

function load_options() {
    myDiv = document.getElementById('period');
    for (var p in period) {
        var opt = document.createElement('option');
        opt.value=p;
        opt.text=p + ' days';
        opt.selected='selected';
        myDiv.appendChild(opt);
    }
}

function loadAll() {
    load_checkboxes()
    load_options()
}