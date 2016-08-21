/**
 * Created by milesg on 8/11/16.
 */

var Button = ReactBootstrap.Button;
var Modal = ReactBootstrap.Modal;
var OverlayTrigger = ReactBootstrap.OverlayTrigger;
var Popover = ReactBootstrap.Popover;
var Tooltip = ReactBootstrap.Tooltip;
var Form = ReactBootstrap.Form;
var FormGroup = ReactBootstrap.FormGroup;
var Col = ReactBootstrap.Col;
var Row = ReactBootstrap.Row;
var Grid = ReactBootstrap.Grid;

class ContactForm extends  React.Component {
    constructor(props){
        super(props);
    }

    render () {
        const popover = (
          <Popover id="modal-popover" title="popover">
            very popover. such engagement
          </Popover>
        );
        const tooltip = (
          <Tooltip id="modal-tooltip">
            wow.
          </Tooltip>
        );

        return (
            <div className="row">
                <div className="col-xs-4 col-xs-offset-4">
                <Modal {...this.props} style={{'margin-top': '10%'}}>
                    <Modal.Header closeButton>
                        <Modal.Title>Contact us</Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        <form>
                            <div className="form-group">
                                <label htmlFor="email">Your email</label>
                                <input name="email" className="form-control" type="email"/>
                            </div>
                            <div className="form-group">
                                <label name="message" htmlFor="message">Message</label>
                                <textarea name="message" rows="5" className="form-control" type="text"/>
                            </div>
                            <div className="form-group text-center">
                                <button type="button" className="btn btn-primary">Send!</button>
                            </div>
                        </form>
                    </Modal.Body>
                    <Modal.Footer>
                        <Button onClick={this.props.onHide}>Cancel</Button>
                    </Modal.Footer>
                </Modal>
                </div>
                </div>
        )
    }
}


class AreaDetail extends  React.Component {
    constructor(props){
        super(props);
    }

    render () {
        const popover = (
          <Popover id="modal-popover" title="popover">
            very popover. such engagement
          </Popover>
        );
        const tooltip = (
          <Tooltip id="modal-tooltip">
            wow.
          </Tooltip>
        );

        return (
            <div className="row">
                <div className="col-xs-4 col-xs-offset-4">
                <Modal bsSize="lg" {...this.props}>
                    <Modal.Header closeButton>
                        <Modal.Title>{this.props.area.title}</Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        <div dangerouslySetInnerHTML={{__html: this.props.area.text}}>
                        </div>
                    </Modal.Body>
                    <Modal.Footer>
                        <Button onClick={this.props.onHide}>Close</Button>
                    </Modal.Footer>
                </Modal>
                </div>
                </div>
        )
    }
}


class BusinessAreaOverview extends React.Component {
    constructor(props){
        super(props);
    }

    render (){

        var passInfoToParent = () => {
            this.props.handleClick(this.props.id);
        };

        return (


            <Col md={4}>
                <div style={{'min-height':'20%'}} className="well">
                    <i className={this.props.glyphicon}> </i>
                    <h4>{this.props.title}</h4>
                    <button onClick={passInfoToParent} className="btn btn-info">Learn more.</button>
                </div>
            </Col>
        )
    }
}



class Main extends React.Component {

    constructor(props){
        super(props);
        this.successful = false;
        this.serverData = null;
        this.state = {
            view: 'home',
            serverData: null,
            showContactForm: false,
            showAreaDetail: false
        };
    }

    getData() {
        var assign = (data) => {
            this.serverData = data.data;
            console.log(this.serverData);
        };

        var url = window.location + '';
        $.ajax({
            url: url,
            data: {'json': true},
            type: 'get',
            dataType: 'json',
            success: function (data) {
                assign(data);
            },
            error: function (error, xhr) {
                console.log(xhr + '  ' + error);
            }
        });
    }
    componentDidMount(){
        console.log('Mounted');
        document.getElementById('home-link').addEventListener('click', function(){ this.setState({view: 'home'})}.bind(this));
        document.getElementById('contact-us').addEventListener('click', function(){this.setState({showContactForm: true})}.bind(this));

        this.getData();

        // Hide loading gif and show app's container
        $('#gears-loader').hide();
        $('#container-div').show();

    }
    componentWillUnmount (){
    }

    componentDidUpdate (){
        this.props.adjustSizes();
    }

    contactUs (){

        var close = () => this.setState({showContactForm: false});
        return(
            <ContactForm show={true} onHide={close}  />
        )

    }

    renderHome() {
        return(
                <div className="row">
                    <div className="col-md-12">
                        <div className="well well-md text-center">
                            <h3>There's a lot of data out there.</h3>
                            <h4>Let's make sense of it.</h4>
                            <hr/>
                            <button onClick={() => {
                                return this.setState({view: 'areas'})
                            }} className="btn btn-primary" value="Find out more">Find out more.
                            </button>
                        </div>
                    </div>
                </div>

    )
    }

    renderAreas () {

        // If user clicks on area overview, change to detail view of that area
        var handleClick = (areaid) => {
            this.showAreaDetailIndex = areaid;
            this.setState({showAreaDetail: true})
        };

        return (
            <Grid fluid={true}>
                <Row>
                    <Col md={12} className="text-center">
                        <h3>
                            Areas of specialty
                        </h3>
                        <hr/>
                        </Col>
                </Row>

                <Row className="text-center">

                    {
                        this.serverData.business_areas.map(function(area, i){
                            console.log(area.title);
                            return(
                                <BusinessAreaOverview handleClick={handleClick}
                                                      title={area.title}
                                                      glyphicon={area.glyphicon}
                                                      id={i}
                                                      key={i} />
                                )

                        })
                    }
                </Row>
            </Grid>
            )
    }

    render () {

        var close = () => {
            $('#container-div').show();
            this.setState({ showAreaDetail: false })
        };


        // ------ Contact form view
        if (this.state.showContactForm) {
            return this.contactUs();
        }


        // ---------Checks for business area detail views ------------
        else if (this.state.showAreaDetail){
            return (
                <AreaDetail area={this.serverData.business_areas[this.showAreaDetailIndex]}
                            show={true}
                            onHide={close} />
            )
        }


        // --------- Checks for base page views --------------
        else if (this.state.view == 'home'){
            return this.renderHome();
        }
        else if (this.state.view == 'areas'){
            return this.renderAreas();
        }


    } // End of main render funct
}

$(document).ready(function(){


    // Dynamically adjust sizes if window changes.
    const adjustSizes = function(){
        var windowHeight = $(window).height();
        var navbarHeight = $('#nav-bar').height();
        var footerHeight = $('#footer').height();
        var containerHeight = $('#container-div').height();

        console.log('adjust func');
        // Stretch particles background all the way
        $('#particles-js').css({'height': windowHeight - navbarHeight - footerHeight });

        // Center gear loading gif.
        $('#gears-loader').css({'margin-top': parseInt(windowHeight / 3)});
    };


    window.addEventListener('resize', adjustSizes);
    adjustSizes(); // Call initially


    // Render main React component
    ReactDOM.render(<Main adjustSizes={adjustSizes} />, document.getElementById('app'));

});
