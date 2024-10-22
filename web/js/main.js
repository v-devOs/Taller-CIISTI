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
    console.log({ data }, "Todos los registros");
  });
}

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
