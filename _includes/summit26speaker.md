  <div class="col-sm-3 col-6 mb-4">
    <div class="row">
      <div class="col-md-12 text-center">
        <img src="media/speakers/{{ speaker.PictureFileName }}" alt="{{ speaker.FirstName }} {{ speaker.LastName }}" class="img-fluid rounded-circle" style="width: 75%">
      </div>
    </div>
    <div class="row">
      <div class="col-md-12 text-center">
        <div class="pt-2">
{% if talk %}
          <a class="speaker" href="#{{ speaker.FirstName }}-{{ speaker.LastName }}-talk">
{% endif %}
	      <h5 class="mt-4 font-weight-medium mb-1"><b>{{ speaker.FirstName }} {{ speaker.LastName }}</b><br>{{ speaker.Company }}</h5>
          <h6 class="subtitle">{{ speaker.Position }}</h6>
{% if talk %}
          </a>
{% endif %}
        </div>
      </div>
    </div>
  </div>
