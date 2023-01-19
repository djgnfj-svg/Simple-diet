import './App.css';
import './temp.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import MyNavbar from './components/navbar';
import Input_form from './pages/body_info_input/input_form/input_form';
import Output_form from './pages/body_info_output/body_info_output';
import { Routes, Route, Link, useNavigate, Outlet } from 'react-router-dom'
import Diet_meal_list from './pages/diet_meal_list/diet_meal_list';
function App() {
  return (
    <div className="app">
      <MyNavbar />
      <Routes>
        <Route path="/" element={<Input_form />} />
        <Route path="*" element={ <div>없는페이지임</div> } />
        <Route path="output" element={<Output_form />} />
        <Route path="diet_meal_list" element={<Diet_meal_list />}>

        </Route>
      </Routes>
    </div>
  );
}

export default App;
