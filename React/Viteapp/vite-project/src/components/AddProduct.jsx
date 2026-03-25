import React from 'react'
import data from '../data/db.json'
const AddProduct = () => {
    const [name, setName] = React.useState('');
    const [price, setPrice] = React.useState('');
    const [category, setCategory] = React.useState('');
    const handleSubmit = (e) => {
        e.preventDefault();
        const newProduct = {
            id: data.products.length + 1,
            name: name,
            price: parseFloat(price),
            category: category
        };
        data.products.push(newProduct);
        alert(`Product added: ${name}, Price: ${price}, Category: ${category}`);
        setName('');
        setPrice(0);
        setCategory('');
        // Here you would typically call an API to add the product or update the local state
    };
  return (
    <div>
      <h2>Add Product</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="price">Price:</label>
          <input
            type="number"
            id="price"
            value={price}
            onChange={(e) => setPrice(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="category">Category:</label>
          <input
            type="text"
            id="category"
            value={category}
            onChange={(e) => setCategory(e.target.value)}
          />
        </div>
        <button type="submit">Add Product</button>
      </form>
    </div>
  )
}

export default AddProduct