import './App.css';
import './temp.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import MyNavbar from './components/navbar';
import Input_form from './pages/body_info_input/input_form/input_form';
import { Routes, Route, Link, useNavigate, Outlet } from 'react-router-dom'
import Output_form from './pages/body_info_output/bodt_info_output';
function App() {
  return (
    <div className="app">
      <MyNavbar />
      <Routes>
        <Route path="/" element={<Input_form />} />
        <Route path="*" element={ <div>없는페이지임</div> } />
        <Route path="output" element={<Output_form />}>

        </Route>
      </Routes>
    </div>
  );
}

export default App;
