<script setup>
import { ref } from 'vue';
import ProductList from '../components/ProductList.vue';
import ProductForm from '../components/ProductForm.vue';

const authToken = 'SEU_TOKEN_AQUI'; // <<<--- NÃO SE ESQUEÇA DE COLOCAR SEU TOKEN

const productListRef = ref(null);
const productFormRef = ref(null);

const handleDataChanged = () => {
  if (productListRef.value) {
    productListRef.value.fetchProducts();
  }
};

const handleProductEdit = (product) => {
  if (productFormRef.value) {
    productFormRef.value.loadProductForEdit(product);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
};

const handleProductDelete = async (productId) => {
  if (confirm(`Tem certeza que deseja excluir o produto com ID ${productId}?`)) {
    try {
      const response = await fetch(`http://127.0.0.1:8000/api/products/${productId}/`, {
        method: 'DELETE',
        headers: { 'Authorization': `Token ${authToken}` }
      });
      if (!response.ok) throw new Error('Falha ao excluir o produto');
      alert('Produto excluído com sucesso!');
      handleDataChanged();
    } catch (error) {
      console.error(error);
      alert('Não foi possível excluir o produto.');
    }
  }
};
</script>

<template>
  <div class="products-view">
    <ProductForm ref="productFormRef" @product-saved="handleDataChanged" />
    <hr>
    <ProductList ref="productListRef" @edit-product="handleProductEdit" @delete-product="handleProductDelete" />
  </div>
</template>

<style scoped>
.products-view { display: flex; flex-direction: column; gap: 20px; }
hr { border: 0; height: 1px; background: #ddd; }
</style>