import './App.css';
import './temp.css';
import Input_form from './components/input/input_form';
import 'bootstrap/dist/css/bootstrap.min.css';
import MyNavbar from './components/navbar';

function App() {
  return (
    <div className="app">
      <MyNavbar></MyNavbar>

      <Input_form></Input_form>
    </div>
  );
}

export default App;
