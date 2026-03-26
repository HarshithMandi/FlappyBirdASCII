import { useEffect, useState } from 'react'

type Product = {
	id: number
	title: string
	price: number
	category: string
	description: string
	image: string
}

const AddPost = () => {
	const [products, setProducts] = useState<Product[]>([])
	const [isLoading, setIsLoading] = useState(true)
	const [error, setError] = useState<string | null>(null)

	useEffect(() => {
		let isMounted = true

		const loadProducts = async () => {
			try {
				const response = await fetch('https://fakestoreapi.com/products')
				if (!response.ok) {
					throw new Error('Unable to load products.')
				}
				const data = (await response.json()) as Product[]
				if (isMounted) {
					setProducts(data)
					setError(null)
				}
			} catch (fetchError) {
				if (isMounted) {
					setError(
						fetchError instanceof Error
							? fetchError.message
							: 'Unable to load products.',
					)
				}
			} finally {
				if (isMounted) {
					setIsLoading(false)
				}
			}
		}

		loadProducts()

		return () => {
			isMounted = false
		}
	}, [])

	return (
		<section className="product-panel">
			<h3>Product listings</h3>
			<p>Available after login.</p>
			{isLoading ? <p>Loading products...</p> : null}
			{error ? (
				<p role="alert">{error}</p>
			) : null}
			{!isLoading && !error ? (
				<ul className="product-list">
					{products.map((product) => (
							<li key={product.id} className="product-card">
								<div className="product-header">
								<div>
									<h4>{product.title}</h4>
										<p className="product-meta">
										{product.category} · ${product.price.toFixed(2)}
									</p>
								</div>
								<img
									src={product.image}
									alt={product.title}
									width={64}
									height={64}
									loading="lazy"
								/>
							</div>
							<p className="product-body">{product.description}</p>
						</li>
					))}
				</ul>
			) : null}
		</section>
	)
}

export default AddPost
