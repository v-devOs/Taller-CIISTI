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

function createCardsTasks(data = []) {
  console.log({ data });
  containerTasks.innerHTML = data.map(
    (item) =>
      ` 
        <div id='${item[0]}' class='card p-5 radius-5'>
          <div class='flex justify-between align-center'>
            <h4>${item[1]}</h4>
          </div>

          <hr/>

          <div class='card-body p-5 radius-5'>
            <div>
              <p>Descipción</p>
              <p>${item[2]}</p>
            </div>
            <div>
              <p>Fecha</p>
              <p>${typeof item[2] == "boolean" ? item[3] : item[2]}</p>
            </div>
          </div>

          <button>Enviar</button>
        </div>
      `
  );

  const cards = document.getElementsByClassName("card");

  const card = cards.item(0);

  card.addEventListener("dblclick", () => card.classList.add("complete"));

  for (const card in cards) {
    console.log(card);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  getAllRegisters();
});

// Funciones Expuestas
function getAllRegisters() {
  eel.get_all_registers()(function (data) {
    info.registers = data;
    createCardsTasks(data);
  });
}

function getOneRegister(id) {
  eel.get_one_by_id(id)(function (data) {
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

function markTaskAsComplete(id) {
  eel.mark_complete(id);
}

// Funciones adicionales
