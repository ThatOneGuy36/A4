
// When the user clicks the 'add student' button, make the form appear and disable the other buttons
function addStudent(){
	document.getElementById("addForm").removeAttribute("hidden");
	document.getElementById("deleteStudent").disabled = true;
	document.getElementById("updateStudent").disabled = true;
}

// When the user clicks the 'delete student' button, make the form appear and disable the other buttons
function deleteStudent(){
	document.getElementById("deleteForm").removeAttribute("hidden");
	document.getElementById("addStudent").disabled = true;
	document.getElementById("updateStudent").disabled = true;
}

// When the user clicks the 'update student' button, make the form appear and disable the other buttons
function updateStudent(){
	document.getElementById("updateForm").removeAttribute("hidden");
	document.getElementById("addStudent").disabled = true;
	document.getElementById("deleteStudent").disabled = true;
}

window.onload = function(){
    document.getElementById("addStudent").addEventListener("click", function(){
		addStudent();
	});
	
	document.getElementById("deleteStudent").addEventListener("click", function(){
		deleteStudent();
	});
	
	document.getElementById("updateStudent").addEventListener("click", function(){
		updateStudent();
	});
}