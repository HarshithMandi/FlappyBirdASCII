class Car{
    engine: string;
    constructor(engine: string){
        this.engine = engine;
    }
    start(){
        console.log("Engine " + this.engine + " is starting.");     

    }
}



export default Car;