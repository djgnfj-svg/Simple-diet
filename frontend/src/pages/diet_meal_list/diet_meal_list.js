import "./diet_meal_list.css"


function Diet_meal_list() {
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
                                <figcaption>Brohm Lake</figcaption>
                            </figure>
                            <ul>
                                <li>Detail 1</li>
                                <li>Detail 2</li>
                                <li>Detail 3</li>
                                <li>Detail 4</li>
                                <li>Detail 5</li>
                            </ul>
                        </div>
                        <div className="card-back">
                            <figure>
                                <div className="img-bg" />
                                <img src="https://images.unsplash.com/photo-1486162928267-e6274cb3106f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60" alt="Brohm Lake" />
                            </figure>
                            <button>Book</button>
                            <div className="design-container">
                                <span className="design design--4" />
                                <span className="design design--5" />
                                <span className="design design--6" />
                                <span className="design design--7" />
                                <span className="design design--8" />
                            </div>
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
                                <figcaption>Légende</figcaption>
                            </figure>
                            <ul>
                                <li>Detail 1</li>
                                <li>Detail 2</li>
                                <li>Detail 3</li>
                                <li>Detail 4</li>
                                <li>Detail 5</li>
                            </ul>
                        </div>
                        <div className="card-back">
                            <figure>
                                <div className="img-bg" />
                                <img src="https://images.unsplash.com/photo-1545436864-cd9bdd1ddebc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60" alt="image-2" />
                            </figure>
                            <button>Book</button>
                            <div className="design-container">
                                <span className="design design--1" />
                                <span className="design design--2" />
                                <span className="design design--3" />
                                <span className="design design--4" />
                                <span className="design design--5" />
                                <span className="design design--6" />
                                <span className="design design--7" />
                                <span className="design design--8" />
                            </div>
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
                                <figcaption>Brohm Lake</figcaption>
                            </figure>
                            <ul>
                                <li>Detail 1</li>
                                <li>Detail 2</li>
                                <li>Detail 3</li>
                                <li>Detail 4</li>
                                <li>Detail 5</li>
                            </ul>
                        </div>
                        <div className="card-back">
                            {/* only if the image is necessary */}
                            <figure>
                                <div className="img-bg" />
                                <img src="https://images.unsplash.com/photo-1486162928267-e6274cb3106f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60" alt="Brohm Lake" />
                            </figure>
                            <button>Book</button>
                            {/* can add svg here and remove these eight spans */}
                            <div className="design-container">
                                <span className="design design--1" />
                                <span className="design design--2" />
                                <span className="design design--3" />
                                <span className="design design--4" />
                                <span className="design design--5" />
                                <span className="design design--6" />
                                <span className="design design--7" />
                                <span className="design design--8" />
                            </div>
                        </div>
                    </div>
                </div >
            </div>
        </>
    )
}

export default Diet_meal_list;
