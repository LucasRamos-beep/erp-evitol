<script setup>
import { reactive, onMounted } from 'vue';

const stats = reactive({
  total_sales_value: 0,
  open_orders_count: 0,
  customer_count: 0,
  low_stock_products_count: 0,
});

// Lembre-se de colocar seu token real aqui
const authToken = '8746734bd796f78ff7b84b83b1eec72bc3031793'; // <<<--- COLOQUE SEU TOKEN AQUI  

onMounted(async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/dashboard/', {
      headers: {
        'Authorization': `Token ${authToken}`
      }
    });

    if (!response.ok) {
      throw new Error('Erro ao buscar dados do dashboard. Verifique o backend e o token.');
    }

    const data = await response.json();

    stats.total_sales_value = data.total_sales_value;
    stats.open_orders_count = data.open_orders_count;
    stats.customer_count = data.customer_count;
    stats.low_stock_products_count = data.low_stock_products_count;

  } catch (error) {
    console.error("Erro no Dashboard.vue:", error);
    alert(error.message);
  }
});
</script>

<template>
  <div class="dashboard-container">
    <h2>Dashboard</h2>
    <div class="dashboard-grid">
      <div class="card">
        <h3>Vendas Totais (R$)</h3>
        <span>{{ stats.total_sales_value.toFixed(2) }}</span>
      </div>
      <div class="card">
        <h3>Pedidos Abertos</h3>
        <span>{{ stats.open_orders_count }}</span>
      </div>
      <div class="card">
        <h3>Total de Clientes</h3>
        <span>{{ stats.customer_count }}</span>
      </div>
      <div class="card">
        <h3>Estoque Baixo</h3>
        <span>{{ stats.low_stock_products_count }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
}
.card {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.card h3 { margin-top: 0; font-size: 1.2em; color: #555; }
.card span {
  font-size: 2.5em;
  font-weight: bold;
  color: #007bff;
}
</style>