<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Electronics</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button
          type="button"
          class="btn btn-success btn-sm"
          @click="toggleAddElectronicsModal">
          Add Electronic
        </button>        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Price</th>
              <th scope="col">Stock</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(electronics, index) in electronics" :key="index">
              <td>{{ electronics.nombre }}</td>
              <td>{{ electronics.precio }}</td>
              <td>{{ electronics.stock }}</td>
              <td>
  <div class="btn-group btn-group-sm" role="group">
    <button
      type="button"
      class="btn btn-outline-success"
      @click="increaseStock(index)">
      + Stock
    </button>
    <button
      type="button"
      class="btn btn-outline-secondary"
      @click="decreaseStock(index)">
      - Stock
    </button>
  </div>
</td>
<td>
  <span
    class="badge"
    :class="electronics.stock > 0 ? 'bg-success' : 'bg-danger'"
    style="margin-left: 10px;">
    {{ electronics.stock > 0 ? 'Disponible' : 'No disponible' }}
  </span>
</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div
  ref="addElectronicsModal"
  class="modal fade"
  :class="{ show: activeAddElectronicsModal, 'd-block': activeAddElectronicsModal }"
  tabindex="-1"
  role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Add a new electronic</h5>
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
              @click="toggleAddElectronicsModal">
              <span aria-hidden="true">&times;</span>
            </button>
      </div>
      <div class="modal-body">
        <form>
          <div class="mb-3">
            <label for="addElectronicsName" class="form-label">Name:</label>
            <input
              type="text"
              class="form-control"
              id="addElectronicsName"
              v-model="addElectronicsForm.nombre"
              placeholder="Enter name">
          </div>
          <div class="mb-3">
            <label for="addElectronicsPrice" class="form-label">Price:</label>
            <input
              type="text"
              class="form-control"
              id="addElectronicsPrice"
              v-model="addElectronicsForm.precio"
              placeholder="Enter price">
          </div>
          <div class="mb-3">
            <label for="addElectronicsStock" class="form-label">Stock:</label>
            <input
              type="text"
              class="form-control"
              id="addElectronicsStock"
              v-model="addElectronicsForm.stock"
              placeholder="Enter stock">
          </div>
          <div class="btn-group" role="group">
            <button
              type="button"
              class="btn btn-primary btn-sm"
              @click="handleAddSubmit">
              Submit
            </button>
            <button
              type="button"
              class="btn btn-danger btn-sm"
              @click="handleAddReset">
              Reset
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</div>
<div v-if="activeAddElectronicsModal" class="modal-backdrop fade show"></div>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
  return {
    activeAddElectronicsModal: false,
    addElectronicsForm: {
      nombre: '',
      precio: '',
      stock: '',
    },
    electronics: [],
    message: '',
    showMessage: false,
  };
},
methods: {
  getElectronics() {
    const query = `
      query {
        electronics {
          id
          nombre
          precio
          stock
          disponible
        }
      }
    `;
    axios.post('http://localhost:5001/graphql', { query })
      .then(res => {
        this.electronics = res.data.data.electronics;
      })
      .catch(console.error);
  },
  updateStock(id, amount) {
    const mutation = `
      mutation {
        updateStock(id: "${id}", amount: ${amount}) {
          success
          message
          electronic {
            id
            stock
            disponible
          }
        }
      }
    `;
    return axios.post('http://localhost:5001/graphql', { query: mutation })
      .then(() => this.getElectronics());
  },
  increaseStock(index) {
    const item = this.electronics[index];
    this.updateStock(item.id, 1);
  },
  decreaseStock(index) {
    const item = this.electronics[index];
    if (item.stock > 0) {
      this.updateStock(item.id, -1);
    }
  },
  toggleAddElectronicsModal() {
  this.activeAddElectronicsModal = !this.activeAddElectronicsModal;
  if (!this.activeAddElectronicsModal) {
    this.initForm();
  }
  },
  initForm() {
    this.addElectronicsForm = {
      nombre: '',
      precio: '',
      stock: '',
    };
  },
},
created() {
  this.getElectronics();
}
};
</script>
