import './App.css';
import './temp.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import MyNavbar from './components/navbar';
import Input_form from './pages/body_info_input/input_form/input_form';

function App() {
  return (
    <div className="app">
      <MyNavbar></MyNavbar>
      <Input_form></Input_form>
    </div>
  );
}

export default App;
