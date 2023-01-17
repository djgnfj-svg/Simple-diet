import 'bootstrap/dist/css/bootstrap.min.css';

// https://codepen.io/albizan/pen/mMWdWZ 이 링크를 토대로 간다.
function MyNavbar() {
    return (
        <div className="">
            <nav className="navbar navbar-expand-lg navbar-light p-3">
                <div className="container-fluid">
                    {/* 마진 right 28px */}
                    <a className="navbar-brand" href="#">간단식단</a>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>

                    <div className=" collapse navbar-collapse" id="navbarNavDropdown">
                        <ul className="navbar-nav ">
                            <li className="nav-item">
                                <a className="nav-link mx-2" href="#">후기</a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link mx-2" href="#">글</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        </div>
    );
}

export default MyNavbar;
