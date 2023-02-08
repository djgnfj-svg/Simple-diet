import "./Food_list.css"
import axios from "axios";
import { useEffect, useState } from "react";

// 참고 url https://codepen.io/eyupucmaz/pen/oNbeXOb
function Food_list() {
  const [food_list, setFood_list] = useState();

  const getfood_list = (e) => {
    axios.get("http://127.0.0.1:8000/api/food/")
      .then((e) => {
        setFood_list(e.data)
      })
  }
  useEffect(() => {
    console.log("랜더링?")
  }, [])

  const onkeytest = (e) => {
    if (e.target.value !== '') {
      e.target.classList.add('notEmpty');
    } else {
      e.target.classList.remove('notEmpty');
    }
  }
  return (
    <>
      <div className="row">
        <h1 style={{color : "white"}}>미완입니다.</h1>
        <div className="col-lg-12">
          <div className="form-container">
            <div className="form-group">
              <input name='height' onKeyUp={onkeytest} className="form-control-input"
                required />
              <label className="label-control">음식이름</label>
              <label className="sort_label-text">정렬기준</label>
                <div class="wrapper">
                  <input type="radio" name="sort_nutrient" id="option-3" value={"protein"} />
                  <input type="radio" name="sort_nutrient" id="option-4" value={"carbohydrate"} />
                  <input type="radio" name="sort_nutrient" id="option-5" value={"fat"} />
                  <label for="option-3" class="option option-3">
                    <div class="dot"></div>
                    <span>단백질</span>
                  </label>
                  <label for="option-4" class="option option-4">
                    <div class="dot"></div>
                    <span>탄수화물</span>
                  </label>
                  <label for="option-5" class="option option-5">
                    <div class="dot"></div>
                    <span>지방</span>
                  </label>
                </div>
                <button type="submit" className="form-control-submit-button">검색</button>
            </div>
          </div>
        </div>
      </div>
      <div className="food_list_body">
        <div className="container">
          <div className="food-card">
            <div className="food-card-body">
            </div>
          </div>
          <div className="food-card">
            <div className="food-card-body">
            </div>
          </div>
          <div className="food-card">
            <div className="food-card-body">
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default Food_list;