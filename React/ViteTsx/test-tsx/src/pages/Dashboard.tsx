import AddPost from '../components/AddPost'

const Dashboard = () => {
	return (
		<main className="dashboard">
			<header>
				<h1>Product dashboard</h1>
				<p>Browse products available after login.</p>
			</header>
			<div className="dashboard-grid">
				<AddPost />
			</div>
		</main>
	)
}

export default Dashboard
