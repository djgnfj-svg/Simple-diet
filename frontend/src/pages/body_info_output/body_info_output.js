import { React, useState } from 'react'
import { useLocation, useNavigate } from 'react-router';
import axios from "axios";
import 'bootstrap/dist/css/bootstrap.min.css';
import './body_info_output.css';

function Output_form() {
  const navigate = useNavigate();
  const { state } = useLocation();

  const [diet_cusom, setdiet_custom] = useState({
    total_kcalorie : state.total_kcalorie,
    total_protein : state.total_protein,
    total_fat : state.total_fat,
    total_carbohydrate : state.total_carbohydrate,
    diet_status : "",
    meal_count : "",
  })
  const {total_kcalorie, total_protein, total_fat, total_carbohydrate, diet_status, meal_count} = diet_cusom 
  const _data = { data : state }

  const navigateToOutput = () => {
    axios.post(process.env.REACT_APP_API + "/api/managing-diet/", diet_cusom)
      .then((e) => {
        navigate('/diet-meal_list', { state: e.data });
      })
      .catch(() => {
        alert("실패")
      })
  }

  const nutrient_list = (e) => {
    const result = []
    switch (e) {
      case "breakfast":
        result.push(
          <div className="card">
            <div className="card__side card__side--front-1">
              <div className="card__details">
                <ul>
                  <li>아침</li>
                  <li>칼로리 : {state.breakfast.kcalorie}kcal</li>
                  <li>탄수화물 : {state.breakfast.carbohydrate}g</li>
                  <li>단백질 : {state.breakfast.protein}g</li>
                  <li>지방 : {state.breakfast.fat}g</li>
                </ul>
              </div>
            </div>
          </div>
        )
        return result
      case "lunch":
        result.push(
          <div className="card">
            <div className="card__side card__side--front-1">
              <div className="card__details">
                <ul>
                  <li>점심</li>
                  <li>칼로리 : {state.lunch.kcalorie}kcal</li>
                  <li>탄수화물 : {state.lunch.carbohydrate}g</li>
                  <li>단백질 : {state.lunch.protein}g</li>
                  <li>지방 : {state.lunch.fat}g</li>
                </ul>
              </div>
            </div>
          </div>
        )
        return result
      case "dinner":
        result.push(
          <div className="card">
            <div className="card__side card__side--front-1">
              <div className="card__details">
                <ul>
                  <li>저녁</li>
                  <li>칼로리 : {state.dinner.kcalorie}kcal</li>
                  <li>탄수화물 : {state.dinner.carbohydrate}g</li>
                  <li>단백질 : {state.dinner.protein}g</li>
                  <li>지방 : {state.dinner.fat}g</li>
                </ul>
              </div>
            </div>
          </div>
        )
        return result
    }
  }
  const handleChangeInput = (e) => {
    const { value, name } = e.target
    setdiet_custom({
      ...diet_cusom,
      [name]: value
    })
  }
  return (
    <section className="section-plans" id="section-plans">
      <div className="u-center-text u-margin-bottom-big">
        <h2 className="heading-secondary">
          끼니 정보
        </h2>
        <span>{state.diet_status}를 위해서는 아래정도로 드시는게 좋습니다.</span>
      </div>
      <div className='container'>

      <div className="row">
        <div className="col-1-of-2">
          <div className="card">
            <div className="card__side card__side--front-1">
              <div className="card__details">
                <ul>
                  <li>유지 영양소</li>
                  <li>칼로리 : {state.total_kcalorie}kcal</li>
                  <li>탄수화물 : {state.total_carbohydrate}g</li>
                  <li>단백질 : {state.total_protein}g</li>
                  <li>지방 : {state.total_fat}g</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
      </div>
<>
      <div className="container">
        <div className="row">
          <div className="col-lg-12">
            <div className="form-container">
              <div className="radio-group">
                <label className="label-text" for="diet_status">다이어트 여부</label>
                <div class="wrapper">
                  <input type="radio" name="diet_status" id="option-10" onChange={handleChangeInput} value={0.8} />
                  <input type="radio" name="diet_status" id="option-11" onChange={handleChangeInput} value={1.0} />
                  <label for="option-10" class="option option-10">
                    <div class="dot"></div>
                    <span>다이어트</span>
                  </label>
                  <label for="option-11" class="option option-11">
                    <div class="dot"></div>
                    <span>유지</span>
                  </label>
                </div>
              </div>
              <label className="label-text" for="many_meals">끼니</label>
              <div class="wrapper">
                <input type="radio" name="many_meals" id="option-12" onChange={handleChangeInput} value={2} />
                <input type="radio" name="many_meals" id="option-13" onChange={handleChangeInput} value={3} />
                <label for="option-12" class="option option-12">
                  <div class="dot"></div>
                  <span>2끼</span>
                </label>
                <label for="option-13" class="option option-13">
                  <div class="dot"></div>
                  <span>3끼</span>
                </label>
              </div>
            </div>
          </div>
        </div>
      </div>
</>
      <div className="u-center-text u-margin-top-huge">
        <a onClick={navigateToOutput} className="btn btn--green">쿠팡 식단 계산</a>
        {/* 모달을 만들어야함
        diet_status : "",
        meal_count : "", */}
        {/* todo 추후 쿠팡 식단 계산으로 이동 */}
      </div>
    </section>
  )
}

export default Output_form;
