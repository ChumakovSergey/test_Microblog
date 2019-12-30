function sendMessage(req_data) {
    var json = JSON.stringify(req_data);
    var xhr = new XMLHttpRequest();
    xhr.open("POST", 'messages/', true)
    xhr.setRequestHeader('Content-type', 'application/json; charset=utf-8');
    csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.send(json);
    xhr.addEventListener("readystatechange", () => {
        if (xhr.readyState === 4 && xhr.status === 200) {
            data = JSON.parse(xhr.responseText);
            console.log(xhr.responseText);
            if (data.success === "ok")
                update();
        }
    });
}

function validateForm(form) {
    formData = new FormData(form);
    objects = {};
    verify = true;
    formData.forEach(function (value, key) {
        if (!value)
            verify = false;
        if (key !== 'csrfmiddlewaretoken')
            objects[key] = value;
    });
    return verify ? objects : false;

}

function update() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", 'messages/', true)
    xhr.addEventListener("readystatechange", () => {
        if (xhr.readyState === 4 && xhr.status === 200) {
            data = JSON.parse(xhr.responseText).data;
            message_list = document.getElementById("message_list");
            message_list.innerHTML = "";
            data.forEach(function (value, key) {
                messageDiv = document.createElement('div');
                messageDiv.className = "message";
                textDiv = document.createElement('text');
                textDiv.className = "text";
                textDiv.innerHTML = value.text;
                dateDiv = document.createElement('div');
                dateDiv.className = "message_date";
                dateDiv.innerHTML = value.date;
                messageDiv.appendChild(textDiv);
                messageDiv.appendChild(dateDiv);
                message_list.appendChild(messageDiv);
            });
        }
    });
    xhr.send();
}

document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('send_message').addEventListener('submit', function (event) {
        event.preventDefault();
        data = validateForm(this);
        this.getElementsByTagName('textarea')[0].value = "";
        if (data)
            sendMessage(data);
    });
    update();

});