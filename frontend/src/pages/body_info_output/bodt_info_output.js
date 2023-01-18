import { React, useState } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import { useLocation, useNavigate } from 'react-router';
import './body_info_output.css';

function Output_form() {
    const { state } = useLocation();
    let data = state.meals["1_meals"]
    return (
        <section className="section-plans" id="section-plans">
        <div className="u-center-text u-margin-bottom-big">
          <h2 className="heading-secondary">
            끼니 정보
          </h2>
        </div>
        <div className="row">
          <div className="col-1-of-3">
            <div className="card">
              <div className="card__side card__side--front-1">
                <div className="card__title card__title--1">
                  <i className="fas fa-paper-plane" />
                  <h4 className="card__heading">그림?</h4>
                </div>
                <div className="card__details">
                  <ul>
                    <li>아침</li>
                    <li>칼로리 : {state.meals["1_meals"].kilo_calorie}</li>
                    <li>탄수화물 : 35g</li>
                    <li>단백질 : 20g</li>
                    <li>지방 : 20g</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          <div className="col-1-of-3">
            <div className="card">
              <div className="card__side card__side--front-2">
                <div className="card__title card__title--2">
                  <i className="fas fa-plane" />
                  <h4 className="card__heading">그림</h4>
                </div>
                <div className="card__details">
                  <ul>
                  <li>점심</li>
                    <li>칼로리 : 500kcal</li>
                    <li>탄수화물 : 35g</li>
                    <li>단백질 : 20g</li>
                    <li>지방 : 20g</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          <div className="col-1-of-3">
            <div className="card">
              <div className="card__side card__side--front-3">
                <div className="card__title card__title--3">
                  <i className="fas fa-rocket" />
                  <h4 className="card__heading">그림</h4>
                </div>
                <div className="card__details">
                  <ul>
                  <li>저녁</li>
                    <li>칼로리 : 500kcal</li>
                    <li>탄수화물 : 35g</li>
                    <li>단백질 : 20g</li>
                    <li>지방 : 20g</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="u-center-text u-margin-top-huge">
          {/* todo 추후 쿠팡 식단 계산으로 이동 */}
          <a href="/" className="btn btn--green">Get Started</a>
        </div>
      </section>
    )
}

export default Output_form;
