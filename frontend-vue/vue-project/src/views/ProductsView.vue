<script setup>
import { ref } from 'vue';
import ProductList from '../components/ProductList.vue';
import ProductForm from '../components/ProductForm.vue';

const productListRef = ref(null);

const handleProductSaved = () => {
  if (productListRef.value) {
    productListRef.value.fetchProducts();
  }
};
</script>

<template>
  <div class="products-view">
    <ProductForm @product-saved="handleProductSaved" />
    <hr>
    <ProductList ref="productListRef" />
  </div>
</template>

<style scoped>
.products-view { display: flex; flex-direction: column; gap: 20px; }
hr { border: 0; height: 1px; background: #ddd; }
</style>