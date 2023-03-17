import 'bootstrap/dist/css/bootstrap.min.css';

// https://codepen.io/albizan/pen/mMWdWZ 이 링크를 토대로 간다.
function MyNavbar() {
    return (
        <div className="">
            <nav className="navbar navbar-expand-lg p-3" style={{backgroundColor: "#3537af"}}>
                <div className="container-fluid">
                    <a className="navbar-brand text-white"  href="/">간단식단</a>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>

                    <div className=" collapse navbar-collapse" id="navbarNavDropdown">
                        <ul className="navbar-nav ">
                            {/* <li className="nav-item">
                                <a className="nav-link mx-2 text-white" href="#">후기</a>
                            </li> */}
                            {/* <li className="nav-item">
                                <a className="nav-link mx-2 text-white" href="/food_list">음식리스트</a>
                            </li> */}
                        </ul>
                    </div>
                </div>
            </nav>
        </div>
    );
}

export default MyNavbar;
