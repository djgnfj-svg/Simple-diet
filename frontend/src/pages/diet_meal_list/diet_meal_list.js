import "./diet_meal_list.css"
import 'bootstrap/dist/css/bootstrap.min.css';
import { useLocation } from 'react-router';
function Diet_meal_list() {
    const { state } = useLocation();
    const food_list = (e) => {
        const result = []
        console.log(state.dinner["nutrient"])
        switch (e) {
            case "breakfast":
                for (let i = 0; i < Object.keys(state.breakfast).length - 1; i++) {
                    result.push(<li><a href={state.breakfast[i].food_link}> {state.breakfast[i].food_name}</a> | {state.breakfast[i].food_number}개</li>)
                    result.push(<li>탄 : {state.breakfast[i].carbohydrate}g 단 : {state.breakfast[i].protein}g 지 : {state.breakfast[i].fat}g 칼 : {state.breakfast[i].kcalorie}kcal</li>)
                }
                return result
            case "lunch":
                for (let i = 0; i < Object.keys(state.lunch).length - 1; i++) {
                    result.push(<li><a href={state.lunch[i].food_link}> {state.lunch[i].food_name}</a> | {state.lunch[i].food_number}개</li>)
                    result.push(<li>탄 : {state.lunch[i].carbohydrate}g 단 : {state.lunch[i].protein}g 지 : {state.lunch[i].fat}g 칼 : {state.lunch[i].kcalorie}kcal</li>)
                }
                return result
            case "dinner":
                for (let i = 0; i < Object.keys(state.dinner).length - 1; i++) {
                    result.push(<li><a href={state.dinner[i].food_link}> {state.dinner[i].food_name}</a> | {state.dinner[i].food_number}개</li>)
                    result.push(<li>탄 : {state.dinner[i].carbohydrate}g 단 : {state.dinner[i].protein}g 지 : {state.dinner[i].fat}g 칼 : {state.dinner[i].kcalorie}kcal</li>)
                }
                return result
        }
    }
    return (
        <>
            <div className="flip-body">
                {/* flip-card-container */}
                {
                    Object.keys(state).length === 3
                        ?
                        <div className="flip-card-container" style={{ "-hue": 220 }}>
                            <h1 className="flip_title">아침</h1>
                            <div className="flip-card">
                                <div className="card-front">
                                    <figure>
                                        <div className="img-bg" />
                                        <img src="https://cdn.kormedi.com/wp-content/uploads/2021/08/gettyimages-1194703474-580x439.jpg" alt="Brohm Lake" />
                                        <figcaption>탄 : {state.breakfast["nutrient"].carbohydrate}g 단 : {state.breakfast["nutrient"].protein}g 지 : {state.breakfast["nutrient"].fat}g 칼 : {state.breakfast["nutrient"].kilo_calorie}kcal</figcaption>
                                    </figure>
                                    <ul>
                                        {food_list("breakfast")}
                                    </ul>
                                </div>
                            </div>
                        </div>
                        :
                        <></>
                }
                {/* /flip-card-container */}
                {/* flip-card-container */}
                <div className="flip-card-container" style={{ "-hue": 170 }}>
                    <h1 className="flip_title">점심</h1>
                    <div className="flip-card">
                        <div className="card-front">
                            <figure>
                                <div className="img-bg" />
                                <img src="https://images.unsplash.com/photo-1545436864-cd9bdd1ddebc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60" alt="Image 2" />
                                <figcaption>탄 : {state.lunch["nutrient"].carbohydrate}g 단 : {state.lunch["nutrient"].protein}g 지 : {state.lunch["nutrient"].fat}g 칼 : {state.lunch["nutrient"].kilo_calorie}kcal</figcaption>

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
                    <h1 className="flip_title">저녁</h1>

                    <div className="flip-card">
                        <div className="card-front">
                            <figure>
                                <div className="img-bg" />
                                <img src="https://images.unsplash.com/photo-1486162928267-e6274cb3106f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60" alt="Brohm Lake" />
                                <figcaption>탄 : {state.dinner["nutrient"].carbohydrate}g 단 : {state.dinner["nutrient"].protein}g 지 : {state.dinner["nutrient"].fat}g 칼 : {state.dinner["nutrient"].kilo_calorie}kcal</figcaption>

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
