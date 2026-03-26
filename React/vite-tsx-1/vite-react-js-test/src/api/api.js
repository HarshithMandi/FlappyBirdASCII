// Simple API helpers for the demo app.
// If you have a backend, set `VITE_API_BASE_URL` in your `.env`.

const API_BASE_URL = import.meta.env?.VITE_API_BASE_URL;

const sampleProducts = [
  { id: 1, name: 'Sample Product A', price: 19.99, category: 'General' },
  { id: 2, name: 'Sample Product B', price: 29.99, category: 'General' },
];

export async function getProducts() {
  // If no backend is configured, fall back to sample data so the UI can render.
  if (!API_BASE_URL) {
    return sampleProducts;
  }

  const response = await fetch(`${API_BASE_URL}/products`);
  if (!response.ok) {
    throw new Error(`getProducts failed: ${response.status} ${response.statusText}`);
  }
  return response.json();
}

export async function addProduct(product) {
  if (!API_BASE_URL) {
    // Demo-mode: pretend it succeeded.
    return { success: true, product };
  }

  const response = await fetch(`${API_BASE_URL}/products`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(product),
  });

  if (!response.ok) {
    throw new Error(`addProduct failed: ${response.status} ${response.statusText}`);
  }

  return response.json();
}
