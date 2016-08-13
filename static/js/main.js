/**
 * Created by milesg on 8/11/16.
 */

class WhatWeDoWells extends React.Component {
    render () {
        return (
            <div className="col-sm-3 col-sm-offset-1 well well-small">
                <h4>{this.props.title}</h4>
                <p>{this.props.introduction}</p>
            </div>)
    }
}


class Main extends React.Component {

    constructor(props){
        super(props);
        this.successful = false;
        this.state = {view: 'welcome', serverData: null};
    }

    componentDidMount(){
        console.log('Mounted');
        this.getData();
    }
    componentWillUnmount (){
        console.log('Unmounting');
    }

    getData (){

        switch (this.state.view){
            case 'welcome':
                var end_request = '';
                break;
            default:
                console.log('Unknown view state: ' + this.state.view);
        }

        $.ajax({
            url: window.location + end_request,
            type: 'GET',
            dataType: 'json',
            data: {'json': true},
            success: function(data){
                this.successful = data.successful;
                this.setState({serverData: data.result});
            }.bind(this),
            error: function(err){
                console.log('error: ' + err);
            }.bind(this)
        })
    }

    renderHomePage () {
        return (
            <div>
                <h3>What We Do</h3>
                <div className="row">
                    {
                        this.state.serverData.map(function (o, i) {
                            return (
                                <WhatWeDoWells key={i} introduction={o.introduction} title={o.title}/>
                            )
                        })
                    }
                </div>
            </div>)
    }

    render () {

        // Show homepage
        if (this.state.view == 'welcome' && this.successful) {
            console.log('Rendering homepage!');
            return (
                this.renderHomePage()
            )
        }

        return(<div>Nothing to show!</div>)
    } // End of main render funct
}

ReactDOM.render(<Main />, document.getElementById('app'));