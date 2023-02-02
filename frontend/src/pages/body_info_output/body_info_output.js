import { React, useState } from 'react'
import { useLocation, useNavigate } from 'react-router';
import axios from "axios";
import 'bootstrap/dist/css/bootstrap.min.css';
import './body_info_output.css';

function Output_form() {
  const navigate = useNavigate();
  const { state } = useLocation();
  const _data = { data: state }

  const navigateToOutput = () => {
    axios.post("http://127.0.0.1:8000/api/diet_diet/", _data)
      .then((e) => {
        navigate('/diet_meal_list', { state: e.data });
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
                  <li>칼로리 : {state.breakfast.kilo_calorie}kcal</li>
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
                  <li>칼로리 : {state.lunch.kilo_calorie}kcal</li>
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
                  <li>칼로리 : {state.dinner.kilo_calorie}kcal</li>
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

  return (
    <section className="section-plans" id="section-plans">
      <div className="u-center-text u-margin-bottom-big">
        <h2 className="heading-secondary">
          끼니 정보
        </h2>
        <span>{state.diet_status}를 위해서는 아래정도로 드시는게 좋습니다.</span>
      </div>
      {console.log(state)}
      {
      Object.keys(state).length === 5
      ?
      <div className="row">
        <div className="col-1-of-3">
          {nutrient_list("breakfast")}
        </div>
        <div className="col-1-of-3">
          {nutrient_list("lunch")}
        </div>
        <div className="col-1-of-3">
          {nutrient_list("dinner")}
        </div>
      </div>
      :
      <div className="row">
        <div className="col-1-of-2">
          {nutrient_list("lunch")}
        </div>
        <div className="col-1-of-2">
          {nutrient_list("dinner")}
        </div>
      </div>
      }


      <div className="u-center-text u-margin-top-huge">
        <a onClick={navigateToOutput} className="btn btn--green">쿠팡 식단 계산</a>
        {/* todo 추후 쿠팡 식단 계산으로 이동 */}
      </div>
    </section>
  )
}

export default Output_form;
