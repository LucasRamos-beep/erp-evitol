<script setup>
import { ref } from 'vue';

const emit = defineEmits(['product-saved']);
const authToken = '8746734bd796f78ff7b84b83b1eec72bc3031793'; // <<<--- COLOQUE SEU TOKEN AQUI

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

  try {
    const response = await fetch('http://127.0.0.1:8000/api/products/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Token ${authToken}` },
      body: JSON.stringify(productData)
    });
    if (!response.ok) throw new Error('Erro ao criar produto');
    
    alert('Produto criado com sucesso!');
    name.value = '';
    price.value = '';
    cost.value = '';
    stock_quantity.value = '';
    emit('product-saved');
  } catch (error) {
    console.error(error);
    alert('Falha ao criar o produto.');
  }
};
</script>

<template>
  <div class="form-container">
    <h2>Adicionar Novo Produto</h2>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="name">Nome:</label>
        <input type="text" v-model="name" required>
      </div>
      <div class="form-group">
        <label for="price">Preço:</label>
        <input type="number" step="0.01" v-model="price" required>
      </div>
      <div class="form-group">
        <label for="cost">Custo:</label>
        <input type="number" step="0.01" v-model="cost" required>
      </div>
      <div class="form-group">
        <label for="stock">Estoque Inicial:</label>
        <input type="number" step="0.01" v-model="stock_quantity" required>
      </div>
      <button type="submit">Adicionar Produto</button>
    </form>
  </div>
</template>

<style scoped>
.form-container { background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
.form-group { margin-bottom: 15px; }
.form-group label { display: block; margin-bottom: 5px; }
.form-group input { width: 100%; max-width: 300px; padding: 8px; box-sizing: border-box; }
button { background-color: #28a745; color: white; border:none; padding: 8px 12px; border-radius: 4px; }
</style>