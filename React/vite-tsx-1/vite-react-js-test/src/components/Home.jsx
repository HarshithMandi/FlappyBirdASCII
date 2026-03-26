import { useContext } from "react"
import { AppContext } from "../AppContext";

const Home = () => {
    const { projectTitle } = useContext(AppContext);
    return (
        <div>
            <h1>{projectTitle}</h1>
            <h3>THis is the home page</h3>
        </div>
    )
}

export default Home
