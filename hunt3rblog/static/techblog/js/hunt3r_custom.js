function hunt3r_typewriter(id, data){
    var terminalElement= document.getElementById(id)
    terminalElement.setAttribute('class', 'terminal')
    var time=0

    for(i=0; i<data.length; i++){
        temp = document.createElement('span')
        if(data[i].command) temp.setAttribute('style', 'font-weight: bold;')
        terminalElement.appendChild(temp)
        new Typewriter(temp, {
            cursor: '',
            animateCursor: false,
            typingSpeed: data[i].speed
        }).pauseFor(time).typeString(data[i].line).start()
        temp_time=2*data[i].speed*data[i].line.length
        if(!data[i].command) terminalElement.appendChild(document.createElement('br'))
        time+=temp_time
        
    }
}