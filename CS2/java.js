function playpause(btn,video) {
  var video = document.getElementById('gameplay');
if(video.paused) {
    video.play();
    btn.innerHTML = "Pause"
}
else {
    video.pause();
    btn.innerHTML = "Play"
}
return false;
};


function namememorysession() {
  if (typeof(Storage) !== "undefined") {
    if (localStorage.namememorysession) {
      localStorage.namememorysession =  document.getElementById('name').value ;
    } else {
      localStorage.namememorysession =   document.getElementById('name').value;
    }
    document.getElementById("resultsession").innerHTML = "Your name is: " + localStorage.namememorysession + "!";
    document.getElementById('nameform').style.display = 'none';
  } else {
    document.getElementById("resultsession").innerHTML = "Thw browser does not support local storage";
  }
}

window.twttr = (function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0],
    t = window.twttr || {};
  if (d.getElementById(id)) return t;
  js = d.createElement(s);
  js.id = id;
  js.src = "https://platform.twitter.com/widgets.js";
  fjs.parentNode.insertBefore(js, fjs);

  t._e = [];
  t.ready = function(f) {
    t._e.push(f);
  };
 
  return t;
}(document, "script", "twitter-wjs"));
