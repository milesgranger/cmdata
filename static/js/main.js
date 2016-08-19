/**
 * Created by milesg on 8/11/16.
 */




class Main extends React.Component {

    constructor(props){
        super(props);
        this.successful = false;
        this.state = {view: 'home', serverData: null};
    }

    componentDidMount(){
        console.log('Mounted');
        document.getElementById('find-out-more').addEventListener('click', function(){this.setState({view: 'areas'})}.bind(this));
        document.getElementById('home-link').addEventListener('click', function(){ this.setState({view: 'home'})}.bind(this));
        document.getElementById('contact-us').addEventListener('click', function(){this.contactUs}.bind(this));

    }
    componentWillUnmount (){
        console.log('Unmounting');
    }

    componentDidUpdate (){
        console.log('Updated!');
    }

    contactUs (){

    }

    renderHome() {
        $('#particles').removeAttr('style');
        $('body').css({'background-color': '#00206e'});
        return null;
    }

    renderAreas () {
        $('#particles').css({'display':'none'});
        $('body').css({'background-color': '#FFFFFF'});
        return (
            <div className="row">
                <div className="col-md-12">
                    <div className="jumbotron">
                        <div className="well well-lg">
                            <p>
                                Welcome to the about page!
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        )
    }

    render () {

        if (this.state.view == 'home'){
            return this.renderHome();
        }
        else if (this.state.view == 'areas'){
            return this.renderAreas();
        }


    } // End of main render funct
}

$(document).ready(function(){
    ReactDOM.render(<Main />, document.getElementById('app'));
});
