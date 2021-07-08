const weekdays = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

function proceed () {
    let port = parseInt(document.getElementById("port").value, 10)
    let pump_intensity = parseInt(document.getElementById("intensity").value, 10)
    let start_server = document.getElementById("start_server").checked
    let sch = [[], [], [], [], [], [], []]
    for (let i = 0; i < 7; ++i){
        let v = document.getElementById(weekdays[i]).value
        if (v == ""){
            continue
        }
         for (let value of v.split(",")){
            if (value == undefined){
                continue
            }
            range = value.split("-")
            if (range[0] == undefined){
                continue
            }
            sch[i].push(convertToSeconds(range[0]) + "-" + convertToSeconds(range[1]));
         }
    }
    let params = {
        "version":0,
        "port":port,
        "pump_intensity":pump_intensity,
        "start_server":start_server,
        "schedule": {
            "mon": sch[0],
            "tue": sch[1],
            "wed": sch[2],
            "tue": sch[3],
            "fri": sch[4],
            "sat": sch[5],
            "sun": sch[6]
        }
    };
    const options = {
        method: 'POST',
        body: JSON.stringify( params )  
    };
    result = fetch( '', options ).then(response => {
        if (response.status == 200){
            return response.text();
        }else{
            console.log("Status: " + response.status);
        }
    });

    if (port != window.location.port && !(window.location.port == "" && port == 80)){
        console.log(port)
        console.log(window.location.port)
        window.location.port = port
    }
}

function convertToSeconds(s){
    if (s == undefined || s == null){
        return 0
    }
    let fields = s.split(":")
    return parseInt(fields[0] * 3600, 10) + parseInt(fields[1] * 60, 10) + parseInt(fields[2], 10) 
}

function convertToHours(s){
    parsed = parseInt(s, 10)
    hours = Math.floor(parsed / 3600 % 24)
    minutes = Math.floor((parsed / 60) % 60)
    seconds = Math.floor(parsed % 60)
    ret = ""
    if (hours < 10){
        ret += "0"
    }
    ret += hours + ":"
    if (minutes < 10){
        ret += "0"
    }
    ret += minutes + ":"
    if (seconds < 10){
        ret += "0"
    }
    ret += seconds
    return ret
}

async function load_settings(){
    return (fetch("/settings.json") 
  .then((response) => response.json()) 
  .then((user) => {
    return user;
  }))
}

settings = async function(){
    //wait for the settings to load
    const s = await load_settings()
    //change settings
    document.getElementById("intensity").value = s["pump_intensity"]
    document.getElementById("start_server").checked = s["start_server"]
    document.getElementById("port").value = s["port"]
    for (let i = 0; i < 7; ++i){
        sch = ""
        table = s["schedule"][weekdays[i]]
        for (const v of table){
            let fields = v.split('-')
            sch += convertToHours(fields[0]) + "-" + convertToHours(fields[1])
            sch += ","
        }
        if (sch.length > 0){
            sch = sch.slice(0, -1)
        }
        document.getElementById(weekdays[i]).value = sch
    }
}



settings()
