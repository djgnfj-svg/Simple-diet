import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import MyNavbar from './components/navbar';
import { Routes, Route} from 'react-router-dom'

import Output_form from './pages/body_info_output/body_info_output';
import Diet_meal_list from './pages/diet_meal_list/diet_meal_list';
import Body_info_input from './pages/body_info_input/body_info_input';
import Food_list from './pages/Food_list/Food_list';

function App() {
  return (
    <div className="app">
      <MyNavbar />
      <Routes>
        <Route path="/" element={<Body_info_input />} />
        <Route path="*" element={ <div>없는페이지임</div> } />
        <Route path="output" element={<Output_form />} />
        <Route path="diet_meal_list" element={<Diet_meal_list />} />
        <Route path="food_list" element={<Food_list />} />
      </Routes>
    </div>
  );
}

export default App;
