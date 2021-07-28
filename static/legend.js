// Control the checkboxes

// whole continent

function ContinentCheckbox(element) {
    continent = element.id;

    if (continent == "america") 
        continent = america
    else if (continent == "africa")
        continent = africa
    else if (continent == "asia")
        continent = asia
    else if (continent == "oceania")
        continent = oceania
    else if (continent == "europe")
        continent = europe
    
    if (element.checked)
        arr = view.getViewColumns();
    else
        arr = []

    for (let c = 0; c < continent.length; c++) {
        country = continent[c]

        arr.push(dataTable.getColumnIndex(country));

        if(continent != america && america.includes(country)) {
            ShowOrHide(country, element.id)
        } 
        if(continent != europe && europe.includes(country)) {
            ShowOrHide(country, element.id)
        } 
        if(continent != asia && asia.includes(country)) {
            ShowOrHide(country, element.id)
        } 
        if(continent != africa && africa.includes(country)) {
            ShowOrHide(country, element.id)
        } 
        if(continent != oceania && oceania.includes(country)) {
            ShowOrHide(country, element.id)
        }
        
        x = document.getElementsByName(country)
        for(let i = 0; i < x.length; i++) {
            x[i].checked = element.checked;
        }
    }
    

    if(element.checked) {
        //arr.sort(function(a, b) {return a - b})
        console.log(arr)
        view.setColumns(arr)
    } else {
        console.log(arr)
        view.hideColumns(arr)
    }
    reload_chart('s')
}

// country

function ShowOrHide(element, c=null) {

    if (c!=null) {
        element = document.getElementsByName(element)
        element[0].checked = document.getElementById(c).checked
    } else {
        var aux = element.checked
        element = document.getElementsByName(element.name)
        element[0].checked = aux
    }

	if (element[0].checked) {
        for (let i = 0; i < element.length; i++)
            element[i].checked = true;

        var arr = view.getViewColumns();
        arr.push(dataTable.getColumnIndex(element[0].name));
        //arr.sort(function(a, b) {return a - b;});
        view.setColumns(arr);

    } else {
        for (let i = 0; i < element.length; i++)
            element[i].checked = false;
        arr = [];
        arr.push(dataTable.getColumnIndex(element[0].name));
        view.hideColumns(arr);
    }

    reload_chart('s')

    if(element[0].checked) {
        if (c != "america" && america.includes(element[0].name)) {
            ctrl = true;
            for (let i = 0; i < america.length && ctrl; i++) {
                x = document.getElementsByName(america[i]);
                ctrl = x[0].checked;
            }
            document.getElementById("america").checked = ctrl;
        }
        if (c != "asia" &&  asia.includes(element[0].name)) {
            ctrl = true;
            for (let i = 0; i < asia.length && ctrl; i++) {
                x = document.getElementsByName(asia[i]);
                ctrl = x[0].checked;
            }
            document.getElementById("asia").checked = ctrl;
        }
        if (c != "europe" && europe.includes(element[0].name)) {
            ctrl = true;
            for (let i = 0; i < europe.length && ctrl; i++) {
                x = document.getElementsByName(europe[i]);
                ctrl = x[0].checked;
            }
            document.getElementById("europe").checked = ctrl;
        }
        if (c != "africa" && africa.includes(element[0].name)) {
            ctrl = true;
            for (let i = 0; i < africa.length && ctrl; i++) {
                x = document.getElementsByName(africa[i]);
                ctrl = x[0].checked;
            }
            document.getElementById("africa").checked = ctrl;
        }
        if (c != "oceania" && oceania.includes(element[0].name)) {
            ctrl = true;
            for (let i = 0; i < oceania.length && ctrl; i++) {
                x = document.getElementsByName(oceania[i]);
                ctrl = x[0].checked;
            }
            document.getElementById("oceania").checked = ctrl;
        }
    } else {
        if(c != "america" && america.includes(element[0].name)) {
            document.getElementById("america").checked = false;
        } if(c != "europe" && europe.includes(element[0].name)) {
            document.getElementById("europe").checked = false;
        } if(c != "asia" && asia.includes(element[0].name)) {
            document.getElementById("asia").checked = false;
        } if(c != "africa" && africa.includes(element[0].name)) {
            document.getElementById("africa").checked = false;
        } if(c != "oceania" && oceania.includes(element[0].name)) {
            document.getElementById("oceania").checked = false;
        }
    }
}