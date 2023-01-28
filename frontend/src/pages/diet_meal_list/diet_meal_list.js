import "./diet_meal_list.css"
import 'bootstrap/dist/css/bootstrap.min.css';
import { useLocation } from 'react-router';
function Diet_meal_list() {
    const { state } = useLocation();
    const food_list = (e) => {
        const result = []
        switch (e) {
            case "breakfast":
                for (let i = 1; i < Object.keys(state.breakfast).length; i++) {
                    result.push(<li><a href={state.breakfast[i].food_name}> {state.breakfast[i].food_name}</a> | {state.breakfast[i].food_number}개</li>)
                }
                return result
            case "lunch":
                for (let i = 1; i < Object.keys(state.lunch).length; i++) {
                    result.push(<li><a href={state.lunch[i].food_name}> {state.lunch[i].food_name}</a> | {state.lunch[i].food_number}개</li>)
                }
                return result
            case "dinner":
                for (let i = 1; i < Object.keys(state.dinner).length; i++) {
                    result.push(<li><a href={state.dinner[i].food_name}> {state.dinner[i].food_name}</a> | {state.dinner[i].food_number}개</li>)
                }
                return result
        }
    }
    return (
        <>
            <div className="flip-body">
                {/* flip-card-container */}
                <div className="flip-card-container" style={{ "-hue": 220 }}>
                    <div className="flip-card">
                        <div className="card-front">
                            <figure>
                                <div className="img-bg" />
                                <img src="https://cdn.kormedi.com/wp-content/uploads/2021/08/gettyimages-1194703474-580x439.jpg" alt="Brohm Lake" />
                                <figcaption>아침</figcaption>
                            </figure>
                            <ul>
                                {food_list("breakfast")}
                            </ul>
                        </div>
                    </div>
                </div>
                {/* /flip-card-container */}
                {/* flip-card-container */}
                <div className="flip-card-container" style={{ "-hue": 170 }}>
                    <div className="flip-card">
                        <div className="card-front">
                            <figure>
                                <div className="img-bg" />
                                <img src="https://images.unsplash.com/photo-1545436864-cd9bdd1ddebc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60" alt="Image 2" />
                                <figcaption>점심</figcaption>
                            </figure>
                            <ul>
                                {food_list("lunch")}
                            </ul>
                        </div>
                    </div>
                </div >
                {/* /flip-card-container */}
                {/* flip-card-container */}
                <div className="flip-card-container" style={{ "-hue": 350 }}>
                    <div className="flip-card">
                        <div className="card-front">
                            <figure>
                                <div className="img-bg" />
                                <img src="https://images.unsplash.com/photo-1486162928267-e6274cb3106f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60" alt="Brohm Lake" />
                                <figcaption>저녁</figcaption>
                            </figure>
                            <ul>
                                {food_list("dinner")}
                            </ul>
                        </div>
                    </div>
                </div >
            </div>
        </>
    )
}

export default Diet_meal_list;
