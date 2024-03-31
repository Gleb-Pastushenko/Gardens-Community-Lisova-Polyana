import { Container } from 'react-bootstrap'

import Header from "./components/Header";
import NewsScreen from "./screens/NewsScreen";

function App() {
  return (
    <div className="App">
      <Header />
      <main className="py-3">
        <Container>
          <NewsScreen />
        </Container>
      </main>

    </div>
  );
}

export default App;
