<script setup>
import { ref, onMounted } from 'vue';

const emit = defineEmits(['edit-product', 'delete-product']);

const products = ref([]);
const authToken = '8746734bd796f78ff7b84b83b1eec72bc3031793'; // <<<--- NÃO SE ESQUEÇA DO SEU TOKEN

const fetchProducts = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/products/', {
      headers: { 'Authorization': `Token ${authToken}` }
    });
    if (!response.ok) throw new Error('Erro ao buscar produtos');
    products.value = await response.json();
  } catch (error) {
    console.error(error);
  }
};

onMounted(fetchProducts);

defineExpose({
  fetchProducts
});
</script>

<template>
  <div class="product-list-container">
    <h2>Lista de Produtos</h2>
    <table>
      <thead>
        <tr>
          <th>Nome</th>
          <th>Preço (R$)</th>
          <th>Estoque</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        <tr v-if="products.length === 0">
          <td colspan="4">Nenhum produto encontrado.</td>
        </tr>
        <tr v-for="product in products" :key="product.id">
          <td>{{ product.name }}</td>
          <td>{{ product.price }}</td>
          <td>{{ product.stock_quantity }}</td>
          <td>
            <button class="edit-btn" @click="emit('edit-product', product)">Editar</button>
            <button class="delete-btn" @click="emit('delete-product', product.id)">Excluir</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
table { width: 100%; border-collapse: collapse; margin-top: 20px; }
th, td { padding: 12px 15px; border: 1px solid #ddd; text-align: left; vertical-align: middle; }
th { background-color: #007bff; color: white; }
tbody tr:nth-child(even) { background-color: #f2f2f2; }
button { margin-right: 5px; border: none; padding: 5px 10px; border-radius: 4px; color: white; cursor: pointer; }
.edit-btn { background-color: #ffc107; color: #212529; }
.delete-btn { background-color: #dc3545; }
</style>