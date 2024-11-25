    <script setup>
    const mode = import.meta.env.MODE; // Define default fallback
    </script>

    <template>
    <header>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">FISCAL CODE WEB</a>
        </div>
        </nav>
    </header>
    <main>
        <h1 class="text-center">FISCAL CODE WEB CALCULATOR</h1>
        <hr />
        <div class="container-fluid text-center">
        <div class="row">
            <div class="col" v-if="weatherData">
                <b>LOCATION:</b> {{ weatherData.location }} <br>
                <b>TEMP:</b> {{ weatherData.temp }} °C <br>
                <img v-if=weatherData.imageWeather :src="weatherData.imageWeather" alt=weatherData.imageWeather>
                <p v-else>Image Not Found</p> <br>
                {{ weatherData.description }}
            </div>
            <div class="col-3">
            <div class="input-group mb-3">
                <div class="p-5 text-center border border-success rounded-3">
                <form @submit.prevent="submitForm">
                    <div class="col">
                    <label class="form-label" for="name"><b>Name:</b></label>
                    <input
                        class="form-control"
                        type="text"
                        id="name"
                        v-model="formData.name"
                        required />
                    </div>
                    <div class="col">
                    <label class="form-label" for="surname"><b>Surname:</b></label>
                    <input
                        class="form-control"
                        type="text"
                        id="surname"
                        v-model="formData.surname"
                        required />
                    </div>
                    <div class="col">
                    <label class="form-label" for="date"><b>Birth Date:</b></label>
                    <input
                        class="form-control"
                        type="date"
                        id="date"
                        v-model="formData.date"
                        required />
                    </div>
                    <div
                    class="col"
                    style="margin-top: 0.1rem; border-radius: 0.3rem">
                    <label class="form-label" for="city"><b>Born City:</b></label>
                    <v-select
                        v-model="formData.city"
                        :options="cities"
                        label="common_name"
                        :reduce="(city) => city.common_name"
                        required>
                        <template #search="{ attributes, events }">
                        <input
                            class="vs__search"
                            :required="!formData.city"
                            v-bind="attributes"
                            v-on="events" />
                        </template>
                    </v-select>
                    </div>
                    <div class="col">
                    <label class="form-label" for="sex"><b>Sex:</b></label>
                    <select
                        class="form-select"
                        id="sex"
                        v-model="formData.sex"
                        required>
                        <option value="M">Male</option>
                        <option value="F">Female</option>
                    </select>
                    </div>
                    <div class="mt-4 rounded">
                    <div class="row justify-content-md-center">
                        <div
                        class="alert alert-success"
                        role="alert"
                        v-if="responseData">
                        <h3>
                            <p>
                            Age: <b>{{ responseData.age }}</b>
                            </p>
                        </h3>
                        <h3>
                            <p>
                            Fiscal Code: <b>{{ responseData.fiscal_code }}</b>
                            </p>
                        </h3>
                        <!--<p>Data: {{ responseData.result }}</p>-->
                        </div>
                        <div
                        class="alert alert-danger"
                        role="alert"
                        v-if="errorMessage">
                        <p>{{ errorMessage }}</p>
                        </div>
                    </div>
                    </div>
                    <div class="col-md-12">
                    <button class="btn btn-primary" type="submit">
                        Calculate
                    </button>
                    -
                    <button class="btn btn-warning" onclick="location.reload()">
                        Refresh
                    </button>
                    </div>
                </form>
                </div>
            </div>
            </div>
            <div class="col"></div>
        </div>
        </div>
    </main>
    <hr />
    <footer class="text-center">
        <p>&copy; 2025 Anselmo Baraggia - All Rights Reserved.</p>
        <p>Version: 1.0.0 - {{ mode }} - {{ server_name }}</p>
    </footer>
    </template>

    <script>
    import axios from "axios";
    import VSelect from "vue-select";

    const apiUrl =
    import.meta.env.MODE !== "production"
        ? "http://localhost:8000/api/"
        : import.meta.env.VITE_APP_ROOT_API; // Define default fallback

    // Get weather data
    const  weatherUrl =
    import.meta.env.MODE !== "production"
        ? "http://localhost:8000/weather/"
        : import.meta.env.VITE_APP_ROOT_WEATHER; // Define default fallback

    // Define the main component
    export default {
    components: {
        VSelect,
    },
    data() {
        return {
        formData: {
            name: "",
            surname: "",
            date: "",
            city: "",
            sex: "",
        },
        cities: [],
        responseData: null, // New data property to store response
        errorMessage: null,
        errorCity: null,
        server_name: null,
        weatherData: null,
        };
    },
    created() {
        // Load cities
        axios
        .get(apiUrl + "commons/")
        .then((response) => {
            this.cities = response.data;
        })
        .catch((error) => {
            console.error(error);
            this.errorCity = "Error loading cities";
        });

        // Load server name
        axios
        .get(apiUrl + "server/")
        .then((response) => {
            this.server_name = response.data;
        })
        .catch((error) => {
            console.error(error);
        });

        // Load weather
        axios
        .get(weatherUrl)
        .then((response) => {
            this.weatherData = response.data;
            console.log(response.data);
        })
        .catch((error) => {
            console.error(error);
        });
    },

    methods: {
        submitForm() {
        axios
            .post(apiUrl + "fc/", this.formData)
            .then((response) => {
            this.responseData = response.data; // Store entire response for display
            console.log(response.data); // Manage the response (age, fiscal code)
            })
            .catch((error) => {
            this.errorMessage = error.response.data.message || "Error";
            });
        },
    },
    };
    </script>

    <style scoped>
    :deep() {
    --vs-colors--lightest: rgba(60, 60, 60, 0.26);
    --vs-colors--light: rgba(60, 60, 60, 0.5);
    --vs-colors--dark: #333;
    --vs-colors--darkest: rgba(0, 0, 0, 0.15);

    /* Search Input */
    --vs-search-input-color: #ffffff;
    --vs-search-input-bg: #ffffff;
    --vs-search-input-placeholder-color: #ffffff;

    /* Font */
    --vs-font-size: 1.1rem;
    --vs-line-height: 1.5rem;

    /* Disabled State */
    --vs-state-disabled-bg: rgb(248, 248, 248);
    --vs-state-disabled-color: var(--vs-colors--light);
    --vs-state-disabled-controls-color: var(--vs-colors--light);
    --vs-state-disabled-cursor: not-allowed;

    /* Borders */
    --vs-border-color: var(--vs-colors--lightest);
    --vs-border-width: 1px;
    --vs-border-style: solid;
    --vs-border-radius: 4px;

    /* Actions: house the component controls */
    --vs-actions-padding: 4px 6px 0 3px;

    /* Component Controls: Clear, Open Indicator */
    --vs-controls-color: var(--vs-colors--light);
    --vs-controls-size: 1;
    --vs-controls--deselect-text-shadow: 0 1px 0 #fff;

    /* Selected */
    --vs-selected-bg: #ffffff;
    --vs-selected-color: var(--vs-colors--dark);
    --vs-selected-border-color: var(--vs-border-color);
    --vs-selected-border-style: var(--vs-border-style);
    --vs-selected-border-width: var(--vs-border-width);

    /* Dropdown */
    --vs-dropdown-bg: #ffffff;
    --vs-dropdown-color: inherit;
    --vs-dropdown-z-index: 1000;
    --vs-dropdown-min-width: 160px;
    --vs-dropdown-max-height: 350px;
    --vs-dropdown-box-shadow: 0px 3px 6px 0px var(--vs-colors--darkest);

    /* Options */
    --vs-dropdown-option-bg: #000;
    --vs-dropdown-option-color: var(--vs-dropdown-color);
    --vs-dropdown-option-padding: 3px 20px;

    /* Active State */
    --vs-dropdown-option--active-bg: #3575dd;
    --vs-dropdown-option--active-color: #fff;

    /* Deselect State */
    --vs-dropdown-option--deselect-bg: #fb5858;
    --vs-dropdown-option--deselect-color: #fff;

    /* Transitions */
    --vs-transition-timing-function: cubic-bezier(1, -0.115, 0.975, 0.855);
    --vs-transition-duration: 150ms;
    }
    </style>
