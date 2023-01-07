import 'bootstrap/dist/css/bootstrap.min.css';
import './input_form.css'

function Input_form() {
  const onkeytest = (e) => {
    if (e.target.value !== ''){
      e.target.classList.add('notEmpty');
    } else {
      e.target.classList.remove('notEmpty');
    }
  }
  return (
    <div className="">
      
      <header id="header" className="ex-2-header">
        <div className="container">
          <div className="row">
            <div className="col-lg-12">
              <h1>바디 정보</h1>
              <p>기초 대사량을 계산하여 알맞은 식단을 제공합니다.</p>
              <div className="form-container">
                <form id="signUpForm" data-toggle="validator" data-focus="false">
                  <div className="form-group">
                    <input onKeyUp={onkeytest} type="email" className="form-control-input" id="semail" required/>
                      <label className="label-control" for="semail">키(cm)</label>
                      <div className="help-block with-errors"></div>
                  </div>
                  <div className="form-group">
                    <input onKeyUp={onkeytest} type="text" className="form-control-input" id="sname" required />
                      <label className="label-control" for="sname">몸무게(kg)</label>
                      <div className="help-block with-errors"></div>
                  </div>
                  <div className="form-group">
                    <input onKeyUp={onkeytest} type="text" className="form-control-input" id="spassword" required />
                      <label className="label-control" for="spassword">나이(만)</label>
                      <div className="help-block with-errors"></div>
                  </div>

                  <label for="codepen">성별</label>
                  <div class="wrapper">
                    <input type="radio" name="select" id="option-1" checked />
                    <input type="radio" name="select" id="option-2" />
                    <label for="option-1" class="option option-1">
                      <div class="dot"></div>
                      <span>남성</span>
                    </label>
                    <label for="option-2" class="option option-2">
                      <div class="dot"></div>
                      <span>여성</span>
                    </label>
                  </div>

                  <label for="codepen">활동량</label>
                  <div class="wrapper">
                    <input type="radio" name="select" id="option-1" checked />
                    <input type="radio" name="select" id="option-2" />
                    <label for="option-1" class="option option-1">
                      <div class="dot"></div>
                      <span>집이 최고</span>
                    </label>
                    <label for="option-2" class="option option-2">
                      <div class="dot"></div>
                      <span>평범</span>
                    </label>
                    <label for="option-2" class="option option-2">
                      <div class="dot"></div>
                      <span>활동적</span>
                    </label>
                  </div>
              
                  <label for="codepen">운동량(1주)</label>
                  <div class="wrapper">
                    <input type="radio" name="select" id="option-1" checked />
                    <input type="radio" name="select" id="option-2" />
                    <label for="option-1" class="option option-1">
                      <div class="dot"></div>
                      <span>0회</span>
                    </label>
                    <label for="option-2" class="option option-2">
                      <div class="dot"></div>
                      <span>1~3회</span>
                    </label>
                    <label for="option-2" class="option option-2">
                      <div class="dot"></div>
                      <span>4~6회</span>
                    </label>
                    <label for="option-2" class="option option-2">
                      <div class="dot"></div>
                      <span>7회+</span>
                    </label>
                  </div>


                  <div className="form-group">
                    <button type="submit" className="form-control-submit-button">제출</button>
                  </div>
                  <div className="form-message">
                    <div id="smsgSubmit" className="h3 text-center hidden"></div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </header>
    </div>
  );
}

export default Input_form;
