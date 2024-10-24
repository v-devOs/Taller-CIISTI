const info = {
  status: 0,
  registers: [],
  newRegister: {},
};

// Div de las tareas

// Logica para obtener todos
// Listener envio de datos formulario

function createCardsTasks(data = []) {
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
              <p>${item[3]}</p>
            </div>
          </div>
        </div>
      `
  );
}

// Listener que cargara todos los datos

// Funciones Expuestas -> Deben ser 5 en total

// Funciones adicionales
