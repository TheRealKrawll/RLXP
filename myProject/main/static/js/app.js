$(document).foundation()

/* Function to return random number between 0 and 100 */
function myRandomNum(){
    var max = 101;
    let min = 0;
    let result = Math.floor(Math.random() * (max - min)) + min;
    document.getElementById('randomResult').innerHTML = result;
}


//NOT SURE IF THIS IS CREATING A HUGE STACK WITH RECURSIVE CALLS
function displayCurrentTime(){
    time = new Date();
    hour = time.hour;
    document.getElementById('date').innerHTML = time;  //new Date().getSeconds();
    //callCurrentTime();
    setTimeout('displayCurrentTime()', 1000);
}

