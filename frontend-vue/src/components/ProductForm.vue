<script setup>
import { ref } from 'vue';

const emit = defineEmits(['product-saved']);
const authToken = '8746734bd796f78ff7b84b83b1eec72bc3031793'; // <<<--- NÃO SE ESQUEÇA DO SEU TOKEN

const editingProductId = ref(null);
const name = ref('');
const price = ref('');
const cost = ref('');
const stock_quantity = ref('');

const handleSubmit = async () => {
  const productData = {
    name: name.value,
    price: price.value,
    cost: cost.value,
    stock_quantity: stock_quantity.value,
  };

  const isEditing = !!editingProductId.value;
  const url = isEditing
    ? `http://127.0.0.1:8000/api/products/${editingProductId.value}/`
    : 'http://127.0.0.1:8000/api/products/';
  const method = isEditing ? 'PUT' : 'POST';

  try {
    const response = await fetch(url, {
      method: method,
      headers: { 'Content-Type': 'application/json', 'Authorization': `Token ${authToken}` },
      body: JSON.stringify(productData)
    });
    if (!response.ok) throw new Error(`Erro ao ${isEditing ? 'atualizar' : 'criar'} produto`);
    
    alert(`Produto ${isEditing ? 'atualizado' : 'criado'} com sucesso!`);
    resetForm();
    emit('product-saved');
  } catch (error) {
    console.error(error);
    alert(`Falha ao ${isEditing ? 'atualizar' : 'criar'} o produto.`);
  }
};

const loadProductForEdit = (product) => {
  editingProductId.value = product.id;
  name.value = product.name;
  price.value = product.price;
  cost.value = product.cost;
  stock_quantity.value = product.stock_quantity;
};

const resetForm = () => {
  editingProductId.value = null;
  name.value = '';
  price.value = '';
  cost.value = '';
  stock_quantity.value = '';
};

defineExpose({
  loadProductForEdit
});
</script>

<template>
  <div class="form-container">
    <h2>{{ editingProductId ? 'Editar Produto' : 'Adicionar Novo Produto' }}</h2>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label>Nome:</label>
        <input type="text" v-model="name" required>
      </div>
      <div class="form-group">
        <label>Preço:</label>
        <input type="number" step="0.01" v-model="price" required>
      </div>
      <div class="form-group">
        <label>Custo:</label>
        <input type="number" step="0.01" v-model="cost" required>
      </div>
      <div class="form-group">
        <label>Estoque Inicial:</label>
        <input type="number" step="0.01" v-model="stock_quantity" required>
      </div>
      <button type="submit">{{ editingProductId ? 'Salvar Alterações' : 'Adicionar Produto' }}</button>
      <button type="button" v-if="editingProductId" @click="resetForm">Cancelar Edição</button>
    </form>
  </div>
</template>

<style scoped>
.form-container { background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
.form-group { margin-bottom: 15px; }
.form-group label { display: block; margin-bottom: 5px; }
.form-group input { width: 100%; max-width: 300px; padding: 8px; box-sizing: border-box; }
button { background-color: #28a745; color: white; border: none; padding: 8px 12px; border-radius: 4px; margin-right: 5px; cursor: pointer;}
button[type="button"] { background-color: #6c757d; }
</style>