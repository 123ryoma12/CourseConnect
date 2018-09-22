import React, { Component } from 'react'; 
import ReactTable from "react-table";
import 'react-table/react-table.css';

class App extends Component {
  render() {
    const data = [{
      course: 'COMP1111',
      count: 52,
      rating: {
        difficulty: '5/5',
        usefulness: 5,
      }
    }];

    const columns = [{
      Header: 'Course',
      accessor: 'course' // String-based value accessors!
    }, {
      Header: 'Count',
      accessor: 'count',
      Cell: props => <span className='number'>{props.value}</span> // Custom cell components!
    }, {
      id: 'rating', // Required because our accessor is not a string
      Header: 'ratingDifficulty',
      accessor: d => d.rating.difficulty // Custom value accessors!
    }, {
      Header: props => <span>Usefulness</span>, // Custom header components!
      accessor: 'rating.usefulness'
    }];

    return (
      <ReactTable
        data={data}
        columns={columns}
      />
    );
  }
}
export default App;
