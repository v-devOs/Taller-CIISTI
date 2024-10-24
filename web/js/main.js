const info = {
  status: 0,
  registers: [],
  newRegister: {},
};

// Contenedor de Tareas
const containerTasks = document.getElementById("container-tasks");

// Logica para obtener todos
// Obtener los campos
document.getElementById("form-task").addEventListener("submit", (event) => {
  event.preventDefault();
});

function getAllRegisters() {
  eel.get_all_registers()(function (data) {
    info.registers = data;
    createCardsTasks(data);
  });
}

function createCardsTasks(data = []) {
  console.log({ data });
  containerTasks.innerHTML = data.map(
    (item) =>
      ` 
        <div id='${item[0]}' class='card p-5 radius-5'>
          <div class='flex justify-between align-center'>
            <h4>${item[1]}</h4>
            <a href="/?=${item[0]}">Completar</a>
          </div>
        </div>
      `
  );
}

//

function getOneRegister() {
  eel.get_one_by_id(1)(function (data) {
    console.log({ data }, "Un solo registro");
  });
}

function createNewRegister() {
  eel.create_register(info.newRegister)(function (state) {
    // Condicionar respuesta
  });
}

function updateRegister() {
  eel.update_register(info.newRegister)(function (state) {
    // Condicionar respuesta
  });
}

document.addEventListener("DOMContentLoaded", () => {
  getAllRegisters();
});
