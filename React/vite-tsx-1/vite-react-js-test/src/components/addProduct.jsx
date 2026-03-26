
import React, { useState } from 'react';
import { addProduct } from '../api/api';

const AddProduct = () => {
    const [name, setName] = useState('');
    const [price, setPrice] = useState(0);
    const [category, setCategory] = useState('');

    const [products, setProducts] = useState([]);

    const handleSubmit = async (e) => {
        e.preventDefault();  // Prevent form default action (page refresh)

        const newProduct = {
            id: products.length + 1,  // Generate a new ID
            name: name,
            price: Number(price),
            category: category
        };

        try {
            await addProduct(newProduct);
            alert('Product added successfully!');
        } catch (e) {
            alert('Failed to add product!', e)
        }
        // Update the local state with the new product
        setProducts([...products, newProduct]);

        // Optionally, reset the form
        setName('');
        setPrice(0);
        setCategory('');
    };

    return (
        <div>
            <h1>Add New Product</h1>
            <form onSubmit={handleSubmit}>
                <label>
                    Name:
                    <input
                        type="text"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        required
                    />
                </label>
                <br />
                <label>
                    Price:
                    <input
                        type="number"
                        value={price}
                        onChange={(e) => setPrice(e.target.value)}
                        required
                    />
                </label>
                <br />
                <label>
                    Category:
                    <input
                        type="text"
                        value={category}
                        onChange={(e) => setCategory(e.target.value)}
                        required
                    />
                </label>
                <br />
                <button type="submit">Add Product</button>
            </form>

            <h2>Product List</h2>
            <ul>
                {products.map((product) => (
                    <li key={product.id}>
                        {product.name} - ${product.price} - {product.category}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default AddProduct;
