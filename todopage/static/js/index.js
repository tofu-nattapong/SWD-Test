// buildList()
// function buildList() {
//   let url = "http://127.0.0.1:8000/api/todo-list/";
//   fetch(url)
//     .then((res) => res.json())
//     .then(function (data) {
//       console.log("Data", data);
//     });
// }


buildList()

function buildList() {
    let task = document.getElementById("todo-list");
    let url = "http://127.0.0.1:8000/api/todo-list/";
    fetch(url)
        .then((res) => res.json())
        .then(function (data) {
            let list = data;
            for (let i in list) {
                try {
                    document.getElementById(`task-${i}`).remove();
                } catch (err) {
                    console.log(err);
                }


                let task_class = "task";
                console.log("Data", list[i].title)
                console.log("Completed", list[i].Completed)

                if (list[i].Completed == true) {
                    task_class = "task-suc";
                }
                // let item = ('<div id ="task-'+(i) +'" class = "' + (task_class) + '"' +
                //     '<div class="text-todo">' + (list[i].title) + '</div>'+
                //     '<span class="close" onclick="">&#215;</span> </div>'
                //     );
                var item = `
					<div id="task-${i}" class=${task_class}>
                        <div class="text-todo">
                            ${list[i].title}
                        </div>
                        <span class="close" onclick="">&#215;</span>
                    </div>
					`
                task.innerHTML += item;

                //     try {
                //         document.getElementById(`task-${i}`).remove();
                //     } catch (err) {
                //         console.log(err);
                //     }

            }

        });




}

// var count;
// $(function () {
//     let url = "http://127.0.0.1:8000/api/todo-list/";
//     count = $('li').length;
//     $('button').click(function () {
//         $('ul').append('<li>Item' + (count++) + '</li>');
//         $('#todo-list').append('<div class>'+);
//
//     });
// });


let form = document.getElementById("header");

form.addEventListener("submit", function (e) {
    e.preventDefault();
    console.log("Form Submit");
    let url = "http://127.0.0.1:8000/api/task-create/";
    // นำข้อความที่อยู่ในช่อง input เข้ามาไว้ในตัวแปรชื่อ title
    let title = document.getElementById("title").value;
    fetch(url, {
        method: "POST",
        headers: {
            "Content-type": "application/json",
            "X-CSRFToken": csrftoken,
        },
        // แปลงข้อมูลให้อยู่ในรูป json ที่เป็นเก็บ title เป็น string
        body: JSON.stringify({title: title}),
    }).then(function (res) {
        // เรียก function ขึ้นมาเพื่อสร้าง List ที่เพิ่มเข้ามาใหม่ลงไปใน todo-list หน้าเว็บของเรา
        buildList();
        // Reset ข้อมูลที่เรากรอกใน form
        document.getElementById("form").reset();
    });
});


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie("csrftoken");

function changeStatus(task) {
    console.log("Task", task);
    let completed = !task.Completed;
    let url = `http://127.0.0.1:8000/api/todo-updates/${task.id}`;
    fetch(url, {
        method: "POST",
        headers: {
            "Content-type": "application/json",
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({title: task.title, Completed: completed}),
    }).then(function () {
        buildList();
    });
}



