function onMapClick(e) {
        L.popup()
            .setLatLng(e.latlng)
            .setContent("You clicked the map at " + e.latlng.toString())
            .openOn(map);
    }


function feedback(event){
//    var targ;
//    if(!e) var e = window.Event;
//    if(e.target) targ = e.target;
//    else if(e.srcElement) targ = e.srcElement;
//    alert("Test message");
    event.preventDefault();
    
    var choice  = confirm("Are you sure about submitting feedback?");
//    var choice = confirm(this.getAttribute('value'));
    if(choice){
        var msg = "Thanks for submitting feedback for this event!";
        alert(msg);
        window.location.href = this.getAttribute('href');
    }
    
}